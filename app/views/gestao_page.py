import customtkinter as ctk
from tkinter import messagebox

class GestaoPage(ctk.CTkFrame):
    def __init__(self, master, voltar_callback, db):
        super().__init__(master, fg_color="transparent")
        self.db = db
        ctk.CTkButton(self, text="⬅ Voltar", width=100, command=voltar_callback).pack(anchor="nw", padx=20, pady=20)
        ctk.CTkLabel(self, text="Gerenciamento de Alunos", font=("Arial", 20, "bold")).pack(pady=10)

        self.lista_frame = ctk.CTkScrollableFrame(self, width=600, height=300)
        self.lista_frame.pack(pady=20, padx=20, fill="both", expand=True)
        self.carregar_alunos()

    def carregar_alunos(self):
        for w in self.lista_frame.winfo_children(): w.destroy()
        for aluno in self.db.obter_todos_alunos():
            frame = ctk.CTkFrame(self.lista_frame)
            frame.pack(fill="x", pady=5, padx=10)
            ctk.CTkLabel(frame, text=f"Nome: {aluno[2]} | Usuário: {aluno[1]}").pack(side="left", padx=10)
            ctk.CTkButton(frame, text="Excluir", fg_color="red", width=80,
                          command=lambda id=aluno[0]: self.remover(id)).pack(side="right", padx=10)

    def remover(self, id):
        if messagebox.askyesno("Confirmar", "Tem certeza que deseja excluir este aluno?"):
            self.db.excluir_usuario(id)
            self.carregar_alunos()