import sqlite3
import hashlib

class Database:
    def __init__(self, db_path="database/conecta.db"):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.criar_tabelas()

    def criar_tabelas(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            nome TEXT,
            email TEXT,
            telefone TEXT,
            tipo TEXT,
            foto_path TEXT
        )
        """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS modulos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT,
            conteudo TEXT
        )
        """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS progresso (
            usuario_id INTEGER,
            modulo_id INTEGER,
            concluido INTEGER DEFAULT 0
        )
        """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS quiz (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pergunta TEXT,
            opA TEXT,
            opB TEXT,
            opC TEXT,
            opD TEXT,
            correta TEXT,
            materia TEXT DEFAULT '',
            dificuldade TEXT DEFAULT ''
        )
        """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS resultados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER,
            nota REAL,
            acertos INTEGER,
            total INTEGER,
            data TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS estatisticas (
            pergunta_id INTEGER,
            respostas INTEGER DEFAULT 0,
            acertos INTEGER DEFAULT 0
        )
        """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS chat (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            remetente_id INTEGER,
            mensagem TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """)
        self.conn.commit()

    # --- MÉTODO ADICIONADO PARA CORRIGIR O ERRO ---
    def buscar_todos_usuarios(self):
        self.cursor.execute("SELECT id, username, nome, email, telefone, tipo, foto_path FROM usuarios")
        return self.cursor.fetchall()
    # -----------------------------------------------

    def registrar_usuario(self, username, password, nome, email, telefone, tipo):
        senha_hash = hashlib.sha256(password.encode()).hexdigest()
        try:
            self.cursor.execute("""
                INSERT INTO usuarios (username, password, nome, email, telefone, tipo)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (username, senha_hash, nome, email, telefone, tipo))
            self.conn.commit()
            return True
        except:
            return False

    def validar_login(self, username, password):
        senha_hash = hashlib.sha256(password.encode()).hexdigest()
        self.cursor.execute("""
            SELECT * FROM usuarios
            WHERE username = ? AND password = ?
        """, (username, senha_hash))
        return self.cursor.fetchone()

    def adicionar_modulo(self, titulo, conteudo):
        self.cursor.execute("""
            INSERT INTO modulos (titulo, conteudo)
            VALUES (?, ?)
        """, (titulo, conteudo))
        self.conn.commit()

    def obter_modulos(self):
        self.cursor.execute("SELECT * FROM modulos ORDER BY id DESC")
        return self.cursor.fetchall()

    def excluir_modulo(self, modulo_id):
        self.cursor.execute("DELETE FROM modulos WHERE id = ?", (modulo_id,))
        self.conn.commit()

    def marcar_modulo_concluido(self, usuario_id, modulo_id):
        self.cursor.execute("""
            INSERT OR REPLACE INTO progresso (usuario_id, modulo_id, concluido)
            VALUES (?, ?, 1)
        """, (usuario_id, modulo_id))
        self.conn.commit()

    def obter_progresso(self, usuario_id):
        self.cursor.execute("""
            SELECT modulo_id FROM progresso
            WHERE usuario_id = ? AND concluido = 1
        """, (usuario_id,))
        return [row[0] for row in self.cursor.fetchall()]

    def adicionar_pergunta(self, pergunta, opA, opB, opC, opD, correta, materia="", dificuldade=""):
        self.cursor.execute("""
            INSERT INTO quiz (pergunta, opA, opB, opC, opD, correta, materia, dificuldade)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (pergunta, opA, opB, opC, opD, correta, materia, dificuldade))
        self.conn.commit()

    def obter_perguntas(self):
        self.cursor.execute("SELECT * FROM quiz ORDER BY id DESC")
        return self.cursor.fetchall()

    def excluir_pergunta(self, pergunta_id):
        self.cursor.execute("DELETE FROM quiz WHERE id = ?", (pergunta_id,))
        self.cursor.execute("DELETE FROM estatisticas WHERE pergunta_id = ?", (pergunta_id,))
        self.conn.commit()

    def salvar_resultado_quiz(self, usuario_id, nota, acertos=0, total=0):
        self.cursor.execute("""
            INSERT INTO resultados (usuario_id, nota, acertos, total)
            VALUES (?, ?, ?, ?)
        """, (usuario_id, nota, acertos, total))
        self.conn.commit()

    def salvar_foto_path(self, username, path):
        self.cursor.execute("""
            UPDATE usuarios
            SET foto_path = ?
            WHERE username = ?
        """, (path, username))
        self.conn.commit()

    def obter_foto_path(self, username):
        self.cursor.execute("""
            SELECT foto_path FROM usuarios
            WHERE username = ?
        """, (username,))
        res = self.cursor.fetchone()
        return res[0] if res else None

    def enviar_mensagem(self, remetente_id, mensagem):
        self.cursor.execute("""
            INSERT INTO chat (remetente_id, mensagem)
            VALUES (?, ?)
        """, (remetente_id, mensagem))
        self.conn.commit()

    def obter_mensagens(self):
        self.cursor.execute("""
            SELECT u.nome, c.mensagem
            FROM chat c
            JOIN usuarios u ON u.id = c.remetente_id
            ORDER BY c.id ASC
        """)
        return self.cursor.fetchall()
        
    def obter_todos_alunos(self):
        self.cursor.execute("""
            SELECT id, username, nome, email, telefone, tipo, foto_path
            FROM usuarios
            WHERE tipo = 'aluno'
            ORDER BY nome ASC
        """)
        return self.cursor.fetchall()
        
    def excluir_usuario(self, usuario_id):
        try:
            self.cursor.execute("BEGIN TRANSACTION")
            self.cursor.execute("DELETE FROM usuarios WHERE id = ?", (usuario_id,))
            self.cursor.execute("DELETE FROM progresso WHERE usuario_id = ?", (usuario_id,))
            self.cursor.execute("DELETE FROM resultados WHERE usuario_id = ?", (usuario_id,))
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e