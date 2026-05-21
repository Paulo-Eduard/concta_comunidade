import customtkinter as ctk
from tkinter import messagebox
from app.services.database import Database
from app.views.login_page import LoginPage
from app.views.register_page import RegisterPage
from app.views.home_page import HomePage
from app.views.chatbot_page import ChatbotPage
from app.views.cursos_page import CursosPage
from app.views.quiz_page import QuizPage
from app.views.seguranca_page import SegurancaPage
from app.views.perfil_page import PerfilPage
from app.views.chat_page import ChatPage
from app.views.gestao_page import GestaoPage

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configuração da janela principal
        self.title("Conecta Comunidade")
        self.geometry("800x600")
        
        # Inicializa o banco de dados
        self.db = Database()
        self.usuario_logado = None
        
        # Container principal onde as páginas serão trocadas
        self.container = ctk.CTkFrame(self)
        self.container.pack(fill="both", expand=True)
        
        # Inicia pela tela de Login
        self.mostrar_login()

    def limpar_container(self):
        """Destroi todos os widgets dentro do container para trocar de tela"""
        for w in self.container.winfo_children(): 
            w.destroy()

    def mostrar_login(self):
        self.limpar_container()
        LoginPage(self.container, self.fazer_login, self.mostrar_cadastro).pack(fill="both", expand=True)

    def mostrar_cadastro(self):
        self.limpar_container()
        RegisterPage(self.container, self.fazer_cadastro, self.mostrar_login).pack(fill="both", expand=True)

    def fazer_login(self, u, p):
        res = self.db.validar_login(u, p)
        if res:
            # Estrutura: (id, username, password, nome, email, telefone, tipo, foto_path)
            self.usuario_logado = {"id": res[0], "username": res[1], "nome": res[3], "tipo": res[6]}
            self.mostrar_home()
        else:
            messagebox.showerror("Acesso Negado", "Usuário não encontrado ou senha incorreta!")

    def fazer_cadastro(self, u, p, n, e, t, tipo):
        if self.db.registrar_usuario(u, p, n, e, t, tipo):
            messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
            self.mostrar_login()
        else:
            messagebox.showerror("Erro", "Falha ao cadastrar. Verifique se o usuário já existe.")

    def mostrar_home(self):
        self.limpar_container()
        HomePage(self.container, self.mudar_pagina, self.usuario_logado).pack(fill="both", expand=True)

    def mudar_pagina(self, destino):
        self.limpar_container()
        
        if destino == "chatbot": 
            ChatbotPage(self.container, self.mostrar_home).pack(fill="both", expand=True)
        elif destino == "cursos": 
            CursosPage(self.container, self.mostrar_home, self.usuario_logado, self.db).pack(fill="both", expand=True)
        elif destino == "quiz": 
            QuizPage(self.container, self.mostrar_home, self.usuario_logado, self.db).pack(fill="both", expand=True)
        elif destino == "seguranca": 
            SegurancaPage(self.container, self.mostrar_home, self.usuario_logado, self.db).pack(fill="both", expand=True)
        elif destino == "perfil": 
            PerfilPage(self.container, self.usuario_logado, self.mostrar_home, self.fazer_logout, self.db).pack(fill="both", expand=True)
        elif destino == "chat":
            ChatPage(self.container, self.mostrar_home, self.usuario_logado, self.db).pack(fill="both", expand=True)
        elif destino == "gestao":
            GestaoPage(self.container, self.mostrar_home, self.db).pack(fill="both", expand=True)

    def fazer_logout(self):
        if messagebox.askyesno("Sair", "Deseja realmente sair da conta?"):
            self.usuario_logado = None
            self.mostrar_login()

if __name__ == "__main__":
    try:
        app = App()
        app.mainloop()
    except Exception as e:
        print(f"Erro crítico no sistema: {e}")