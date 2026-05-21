import customtkinter as ctk
from tkinter import messagebox

class RegisterPage(ctk.CTkFrame):
    def __init__(self, master, register_callback, voltar_callback):
        super().__init__(master, fg_color="transparent")
        
        ctk.CTkLabel(self, text="Cadastro de Usuário", font=("Arial", 20, "bold")).pack(pady=20)

        self.nome = ctk.CTkEntry(self, placeholder_text="Nome Completo", width=300)
        self.nome.pack(pady=5)
        
        self.user = ctk.CTkEntry(self, placeholder_text="Usuário (Login)", width=300)
        self.user.pack(pady=5)
        
        self.email = ctk.CTkEntry(self, placeholder_text="E-mail", width=300)
        self.email.pack(pady=5)

        self.tipo = ctk.CTkOptionMenu(self, values=["aluno", "professor"], width=300, command=self.atualizar_visibilidade)
        self.tipo.pack(pady=5)
        
        self.senha = ctk.CTkEntry(self, placeholder_text="Senha", width=300, show="*")
        self.senha.pack(pady=5)
        
        self.chave_admin = ctk.CTkEntry(self, placeholder_text="Chave Secreta (Professores)", width=300, show="*")
        
        ctk.CTkButton(self, text="Finalizar Cadastro", command=self.tentar_cadastro).pack(pady=20)
        ctk.CTkButton(self, text="Voltar", fg_color="gray", command=voltar_callback).pack()

        self.register_callback = register_callback
        self.atualizar_visibilidade("aluno")

    def atualizar_visibilidade(self, escolha):
        if escolha == "professor":
            self.chave_admin.pack(pady=5)
        else:
            self.chave_admin.pack_forget()

    def tentar_cadastro(self):
        tipo = self.tipo.get()
        if tipo == "professor" and self.chave_admin.get() != "1945":
            messagebox.showerror("Erro", "Chave de professor inválida!")
            return
        
        self.register_callback(self.user.get(), self.senha.get(), self.nome.get(), self.email.get(), "000000", tipo)