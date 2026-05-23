#Ideias:
#Colocar o nome do usuário logado no topo da tela, com um ícone de perfil ao lado.
#Botão de logout no canto superior direito, que redireciona para a tela de login. (feito)

import customtkinter as ctk

class HomePage(ctk.CTkFrame):
    def __init__(self, master, navigate_to_callback, usuario_logado, fazer_logout_callback):
        super().__init__(master, fg_color="transparent")
        self.navigate_to = navigate_to_callback
        self.fazer_logout = fazer_logout_callback
        self.usuario = usuario_logado

        # Header 
        self.header = ctk.CTkFrame(self, corner_radius=0, height=50)
        self.header.pack(fill="x", side="top")
        self.header.pack_propagate(False)

        ctk.CTkLabel(self.header, text=f"👤 {self.usuario.get('nome', 'Usuário')}",
                     font=("Arial", 14), text_color="#a0a0b0").pack(side="left", padx=20, pady=10)

        ctk.CTkButton(self.header, text="Sair", width=80, height=30,
                      fg_color="#c0392b", hover_color="#922b21",
                      text_color="white", font=("Arial", 13, "bold"),
                      command=self.fazer_logout).pack(side="right", padx=20, pady=10)

        # Título 
        ctk.CTkLabel(self, text=f"Bem-vindo ao Conecta Comunidade, {self.usuario.get('nome', 'Usuário')}! 🚀",
                     font=("Arial", 28, "bold"), text_color="white").pack(pady=40)

        # Botões do menu
        self.menu_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.menu_frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.criar_botao("📚 Cursos", "cursos")
        self.criar_botao("❓ Quiz de Conhecimento", "quiz")
        self.criar_botao("🤖 Chatbot IA", "chatbot")
        self.criar_botao("🛡️Segurança Digital", "seguranca")
        self.criar_botao("💬 Chat de Contato", "chat")
        self.criar_botao("👤 Meu Perfil", "perfil")

        # Exibe o botão de Gestão apenas para o Professor
        if self.usuario.get('tipo') == 'professor':
            self.criar_botao("📊 Gerenciar Alunos", "gestao")

    def criar_botao(self, texto, destino):
        btn = ctk.CTkButton(self.menu_frame, text=texto, font=("Arial", 16, "bold"), height=50,
                            text_color="white", fg_color="#2d6a9f", hover_color="#1a4f7a",
                            command=lambda: self.navigate_to(destino))
        btn.pack(pady=10, padx=50, fill="x")