import customtkinter as ctk

class HomePage(ctk.CTkFrame):
    def __init__(self, master, navigate_to_callback, usuario_logado):
        super().__init__(master, fg_color="transparent")
        self.navigate_to = navigate_to_callback
        self.usuario = usuario_logado
        
        ctk.CTkLabel(self, text="Bem-vindo ao Conecta Comunidade", font=("Arial", 28, "bold")).pack(pady=40)

        self.menu_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.menu_frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.criar_botao("📚 Cursos", "cursos")
        self.criar_botao("❓ Quiz de Conhecimento", "quiz") 
        self.criar_botao("🤖 Chatbot IA", "chatbot")
        self.criar_botao("🛡️ Segurança Digital", "seguranca")
        self.criar_botao("💬 Chat de Contato", "chat")
        self.criar_botao("👤 Meu Perfil", "perfil")

        # Exibe o botão de Gestão apenas para o Professor
        if self.usuario.get('tipo') == 'professor':
            self.criar_botao("📊 Gerenciar Alunos", "gestao")

    def criar_botao(self, texto, destino):
        btn = ctk.CTkButton(self.menu_frame, text=texto, font=("Arial", 16), height=50,
                            command=lambda: self.navigate_to(destino))
        btn.pack(pady=10, padx=50, fill="x")