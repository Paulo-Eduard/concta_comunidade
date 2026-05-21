import customtkinter as ctk
from tkinter import messagebox

class QuizPage(ctk.CTkFrame):
    def __init__(self, master, voltar_callback, usuario_logado, db):
        super().__init__(master, fg_color="transparent")
        self.db = db
        self.usuario = usuario_logado
        self.voltar = voltar_callback
        
        ctk.CTkButton(self, text="⬅ Voltar", width=100, fg_color="gray", command=self.voltar).pack(anchor="nw", padx=20, pady=20)
        
        if self.usuario.get('tipo') == 'professor':
            self.criar_painel_professor()
        else:
            self.criar_painel_aluno()

    # --- PAINEL PROFESSOR: ADICIONAR E EXCLUIR ---
    def criar_painel_professor(self):
        # Campos de entrada
        self.p = ctk.CTkEntry(self, placeholder_text="Pergunta", width=400)
        self.p.pack(pady=5)
        self.a = ctk.CTkEntry(self, placeholder_text="Opção A", width=400)
        self.a.pack(pady=5)
        self.b = ctk.CTkEntry(self, placeholder_text="Opção B", width=400)
        self.b.pack(pady=5)
        self.c = ctk.CTkEntry(self, placeholder_text="Opção C", width=400)
        self.c.pack(pady=5)
        self.d = ctk.CTkEntry(self, placeholder_text="Opção D", width=400)
        self.d.pack(pady=5)
        self.correta = ctk.CTkEntry(self, placeholder_text="Correta (A, B, C ou D)", width=400)
        self.correta.pack(pady=5)
        
        ctk.CTkButton(self, text="Adicionar Questão", command=self.salvar).pack(pady=10)
        
        # Lista de perguntas para excluir
        self.lista_scroll = ctk.CTkScrollableFrame(self, width=400, height=200)
        self.lista_scroll.pack(pady=10)
        self.atualizar_lista_perguntas()

    def atualizar_lista_perguntas(self):
        for w in self.lista_scroll.winfo_children(): w.destroy()
        perguntas = self.db.obter_perguntas()
        for q in perguntas:
            frame = ctk.CTkFrame(self.lista_scroll)
            frame.pack(fill="x", pady=2)
            ctk.CTkLabel(frame, text=q[1], width=200).pack(side="left", padx=5)
            ctk.CTkButton(frame, text="Excluir", fg_color="red", width=60, 
                          command=lambda id=q[0]: self.deletar_pergunta(id)).pack(side="right")

    def salvar(self):
        self.db.adicionar_pergunta(self.p.get(), self.a.get(), self.b.get(), self.c.get(), self.d.get(), self.correta.get())
        messagebox.showinfo("Sucesso", "Questão adicionada!")
        self.atualizar_lista_perguntas()

    def deletar_pergunta(self, id):
        self.db.excluir_modulo(id) # Certifique-se de que no database.py o método de excluir_pergunta está mapeado
        self.db.cursor.execute("DELETE FROM quiz WHERE id = ?", (id,))
        self.db.conn.commit()
        self.atualizar_lista_perguntas()

    # --- PAINEL ALUNO: RESPONDER ---
    def criar_painel_aluno(self):
        self.perguntas = self.db.obter_perguntas()
        if not self.perguntas:
            ctk.CTkLabel(self, text="Nenhuma pergunta disponível.").pack()
            return
        self.pontos = 0
        self.index = 0
        self.mostrar_pergunta()

    def mostrar_pergunta(self):
        for w in self.winfo_children():
            if w.winfo_class() != "CTkButton": w.destroy()
        
        if self.index < len(self.perguntas):
            q = self.perguntas[self.index]
            ctk.CTkLabel(self, text=f"Pergunta: {q[1]}", font=("Arial", 18)).pack(pady=20)
            for i, opt in enumerate([q[2], q[3], q[4], q[5]]):
                letra = ["A", "B", "C", "D"][i]
                ctk.CTkButton(self, text=f"{letra}: {opt}", command=lambda l=letra: self.responder(l, q[6])).pack(pady=5)
        else:
            self.finalizar()

    def responder(self, res, cor):
        if res == cor: self.pontos += 1
        self.index += 1
        self.mostrar_pergunta()

    def finalizar(self):
        nota = (self.pontos / len(self.perguntas)) * 100
        self.db.salvar_resultado_quiz(self.usuario['id'], nota)
        messagebox.showinfo("Fim!", f"Você acertou {self.pontos}/{len(self.perguntas)}. Nota: {nota}%")
        self.voltar()