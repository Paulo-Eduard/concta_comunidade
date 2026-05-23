
import customtkinter as ctk
from tkinter import messagebox

# =====================================================
# DATABASE
# =====================================================

from app.services.database import Database

# =====================================================
# PÁGINAS
# =====================================================

from app.views.login_page import LoginPage
from app.views.register_page import RegisterPage
from app.views.home_page import HomePage
from app.views.cursos_page import CursosPage
from app.views.quiz_page import QuizPage
from app.views.chatbot_page import ChatbotPage
from app.views.perfil_page import PerfilPage
from app.views.chat_page import ChatPage
from app.views.seguranca_page import SegurancaPage
from app.views.gestao_page import GestaoPage
from app.views.ranking_page import RankingPage


# =====================================================
# APP PRINCIPAL
# =====================================================

class App(ctk.CTk):

    def __init__(self):

        super().__init__()

        # =========================================
        # CONFIGURAÇÃO DA JANELA
        # =========================================

        self.title("Conecta Comunidade")

        self.geometry("1400x850")

        self.minsize(1200, 700)

        self.configure(
            fg_color="#0f172a"
        )

        # =========================================
        # TEMA
        # =========================================

        ctk.set_appearance_mode("dark")

        ctk.set_default_color_theme("blue")

        # =========================================
        # DATABASE
        # =========================================

        self.db = Database()

        # =========================================
        # USUÁRIO
        # =========================================

        self.usuario_logado = None

        # =========================================
        # CONTAINER PRINCIPAL
        # =========================================

        self.container = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.container.pack(
            fill="both",
            expand=True
        )

        # =========================================
        # ABRIR LOGIN
        # =========================================

        self.mostrar_login()

    # =====================================================
    # LIMPAR TELA
    # =====================================================

    def limpar_container(self):

        for widget in self.container.winfo_children():

            widget.destroy()

    # =====================================================
    # LOGIN
    # =====================================================

    def mostrar_login(self):

        self.limpar_container()

        LoginPage(

            self.container,

            self.fazer_login,

            self.mostrar_cadastro

        ).pack(

            fill="both",
            expand=True

        )

    # =====================================================
    # CADASTRO
    # =====================================================

    def mostrar_cadastro(self):

        self.limpar_container()

        RegisterPage(

            self.container,

            self.fazer_cadastro,

            self.mostrar_login

        ).pack(

            fill="both",
            expand=True

        )

    # =====================================================
    # FAZER LOGIN
    # =====================================================

    def fazer_login(self, username, password):

        if not username or not password:

            messagebox.showwarning(
                "Campos vazios",
                "Digite usuário e senha."
            )

            return

        resultado = self.db.validar_login(
            username,
            password
        )

        if resultado:

            self.usuario_logado = {

                "id": resultado[0],

                "username": resultado[1],

                "nome": resultado[3],

                "tipo": resultado[6]

            }

            messagebox.showinfo(
                "Sucesso",
                f"Bem-vindo {self.usuario_logado['nome']}!"
            )

            self.mostrar_home()

        else:

            messagebox.showerror(
                "Erro",
                "Usuário ou senha incorretos."
            )

    # =====================================================
    # FAZER CADASTRO
    # =====================================================

    def fazer_cadastro(
        self,
        username,
        password,
        nome,
        email,
        telefone,
        tipo
    ):

        if (
            not username or
            not password or
            not nome
        ):

            messagebox.showwarning(
                "Campos vazios",
                "Preencha os campos obrigatórios."
            )

            return

        sucesso = self.db.registrar_usuario(

            username,
            password,
            nome,
            email,
            telefone,
            tipo

        )

        if sucesso:

            messagebox.showinfo(
                "Sucesso",
                "Conta criada com sucesso!"
            )

            self.mostrar_login()

        else:

            messagebox.showerror(
                "Erro",
                "Usuário já existe."
            )

    # =====================================================
    # HOME
    # =====================================================

    def mostrar_home(self):

        self.limpar_container()

        HomePage(

            self.container,

            self.mudar_pagina,

            self.usuario_logado,

            self.fazer_logout

        ).pack(

            fill="both",
            expand=True

        )

    # =====================================================
    # MUDAR PÁGINA
    # =====================================================

    def mudar_pagina(self, destino):

        self.limpar_container()

        # =========================================
        # HOME
        # =========================================

        if destino == "home":

            self.mostrar_home()

        # =========================================
        # CURSOS
        # =========================================

        elif destino == "cursos":

            CursosPage(

                self.container,

                self.mudar_pagina,

                self.usuario_logado,

                self.db

            ).pack(

                fill="both",
                expand=True

            )

        # =========================================
        # QUIZ
        # =========================================

        elif destino == "quiz":

            QuizPage(

                self.container,

                self.mudar_pagina,

                self.usuario_logado,

                self.db

            ).pack(

                fill="both",
                expand=True

            )

        # =========================================
        # CHATBOT IA
        # =========================================

        elif destino == "chatbot":

            ChatbotPage(

                self.container,

                self.mudar_pagina

            ).pack(

                fill="both",
                expand=True

            )

        # =========================================
        # PERFIL
        # =========================================

        elif destino == "perfil":

            PerfilPage(

                self.container,

                self.usuario_logado,

                self.mudar_pagina,

                self.fazer_logout,

                self.db

            ).pack(

                fill="both",
                expand=True

            )

        # =========================================
        # CHAT
        # =========================================

        elif destino == "chat":

            ChatPage(

                self.container,

                self.mudar_pagina,

                self.usuario_logado,

                self.db

            ).pack(

                fill="both",
                expand=True

            )

        # =========================================
        # SEGURANÇA
        # =========================================

        elif destino == "seguranca":

            SegurancaPage(

                self.container,

                self.mudar_pagina,

                self.usuario_logado,

                self.db

            ).pack(

                fill="both",
                expand=True

            )

        # =========================================
        # GESTÃO
        # =========================================

        elif destino == "gestao":

            GestaoPage(

                self.container,

                self.mudar_pagina,

                self.db

            ).pack(

                fill="both",
                expand=True

            )

        # =========================================
        # RANKING
        # =========================================

        elif destino == "ranking":

            RankingPage(

                self.container,

                self.mudar_pagina,

                self.db

            ).pack(

                fill="both",
                expand=True

            )

        # =========================================
        # DESTINO INVÁLIDO
        # =========================================

        else:

            messagebox.showerror(
                "Erro",
                f"Página '{destino}' não encontrada."
            )

            self.mostrar_home()

    # =====================================================
    # LOGOUT
    # =====================================================

    def fazer_logout(self):

        confirmar = messagebox.askyesno(

            "Sair",

            "Deseja realmente sair?"

        )

        if confirmar:

            self.usuario_logado = None

            self.mostrar_login()

    # =====================================================
    # FECHAR SISTEMA
    # =====================================================

    def on_close(self):

        try:

            self.db.conn.close()

        except:

            pass

        self.destroy()


# =====================================================
# EXECUTAR
# =====================================================

if __name__ == "__main__":

    try:

        app = App()

        app.protocol(
            "WM_DELETE_WINDOW",
            app.on_close
        )

        app.mainloop()

    except Exception as erro:

        print(
            f"\nERRO CRÍTICO:\n{erro}\n"
        )
