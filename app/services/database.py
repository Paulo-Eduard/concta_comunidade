import sqlite3
import hashlib

class Database:
    def __init__(self, db_path="database/conecta.db"):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.criar_tabelas()

    def criar_tabelas(self):
        # Usuários e Perfis
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            username TEXT UNIQUE NOT NULL, password TEXT NOT NULL, 
            nome TEXT, email TEXT, telefone TEXT, tipo TEXT, foto_path TEXT)""")
        
        # Conteúdos e Cursos
        self.cursor.execute("CREATE TABLE IF NOT EXISTS modulos (id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT, conteudo TEXT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS progresso (usuario_id INTEGER, modulo_id INTEGER, concluido INTEGER DEFAULT 0)")
        
        # Quiz e Resultados
        self.cursor.execute("CREATE TABLE IF NOT EXISTS quiz (id INTEGER PRIMARY KEY AUTOINCREMENT, pergunta TEXT, opA TEXT, opB TEXT, opC TEXT, opD TEXT, correta TEXT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS resultados (usuario_id INTEGER PRIMARY KEY, nota REAL)")
        
        # Chat
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS chat (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            remetente_id INTEGER, 
            mensagem TEXT, 
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)""")
        
        self.conn.commit()

    # --- Usuários e Gestão de Alunos ---
    def registrar_usuario(self, username, password, nome, email, telefone, tipo):
        senha_hash = hashlib.sha256(password.encode()).hexdigest()
        try:
            self.cursor.execute("INSERT INTO usuarios (username, password, nome, email, telefone, tipo) VALUES (?, ?, ?, ?, ?, ?)", (username, senha_hash, nome, email, telefone, tipo))
            self.conn.commit()
            return True
        except: return False

    def validar_login(self, username, password):
        senha_hash = hashlib.sha256(password.encode()).hexdigest()
        self.cursor.execute("SELECT * FROM usuarios WHERE username = ? AND password = ?", (username, senha_hash))
        return self.cursor.fetchone()

    def obter_todos_alunos(self):
        self.cursor.execute("SELECT id, username, nome, email FROM usuarios WHERE tipo = 'aluno'")
        return self.cursor.fetchall()

    def excluir_usuario(self, usuario_id):
        self.cursor.execute("DELETE FROM usuarios WHERE id = ?", (usuario_id,))
        self.cursor.execute("DELETE FROM progresso WHERE usuario_id = ?", (usuario_id,))
        self.cursor.execute("DELETE FROM resultados WHERE usuario_id = ?", (usuario_id,))
        self.conn.commit()

    # --- Fotos ---
    def salvar_foto_path(self, username, path):
        self.cursor.execute("UPDATE usuarios SET foto_path = ? WHERE username = ?", (path, username))
        self.conn.commit()

    def obter_foto_path(self, username):
        self.cursor.execute("SELECT foto_path FROM usuarios WHERE username = ?", (username,))
        res = self.cursor.fetchone()
        return res[0] if res else None

    # --- Chat ---
    def enviar_mensagem(self, remetente_id, texto):
        self.cursor.execute("INSERT INTO chat (remetente_id, mensagem) VALUES (?, ?)", (remetente_id, texto))
        self.conn.commit()

    def obter_mensagens(self):
        self.cursor.execute("SELECT u.nome, c.mensagem FROM chat c JOIN usuarios u ON c.remetente_id = u.id ORDER BY c.id ASC")
        return self.cursor.fetchall()

    # --- Cursos ---
    def adicionar_modulo(self, titulo, conteudo):
        self.cursor.execute("INSERT INTO modulos (titulo, conteudo) VALUES (?, ?)", (titulo, conteudo))
        self.conn.commit()

    def obter_modulos(self):
        self.cursor.execute("SELECT * FROM modulos")
        return self.cursor.fetchall()

    def marcar_modulo_concluido(self, usuario_id, modulo_id):
        self.cursor.execute("INSERT OR REPLACE INTO progresso (usuario_id, modulo_id, concluido) VALUES (?, ?, 1)", (usuario_id, modulo_id))
        self.conn.commit()

    def obter_progresso(self, usuario_id):
        self.cursor.execute("SELECT modulo_id FROM progresso WHERE usuario_id = ? AND concluido = 1", (usuario_id,))
        return [row[0] for row in self.cursor.fetchall()]

    # --- Quiz ---
    def adicionar_pergunta(self, pergunta, opA, opB, opC, opD, correta):
        self.cursor.execute("INSERT INTO quiz (pergunta, opA, opB, opC, opD, correta) VALUES (?, ?, ?, ?, ?, ?)", (pergunta, opA, opB, opC, opD, correta))
        self.conn.commit()

    def obter_perguntas(self):
        self.cursor.execute("SELECT * FROM quiz")
        return self.cursor.fetchall()

    def salvar_resultado_quiz(self, usuario_id, nota):
        self.cursor.execute("INSERT OR REPLACE INTO resultados (usuario_id, nota) VALUES (?, ?)", (usuario_id, nota))
        self.conn.commit()

    def obter_nota(self, usuario_id):
        self.cursor.execute("SELECT nota FROM resultados WHERE usuario_id = ?", (usuario_id,))
        res = self.cursor.fetchone()
        return res[0] if res else 0