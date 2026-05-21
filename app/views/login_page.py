import customtkinter as ctk

class LoginPage(ctk.CTkFrame):
    def __init__(self, master, login_callback, ir_para_cadastro_callback):
        super().__init__(master, fg_color="transparent")
        
        ctk.CTkLabel(self, text="Bem-vindo ao Conecta", font=("Arial", 24, "bold")).pack(pady=40)
        
        self.user = ctk.CTkEntry(self, placeholder_text="Usuário", width=300)
        self.user.pack(pady=10)
        
        self.senha = ctk.CTkEntry(self, placeholder_text="Senha", width=300, show="*")
        self.senha.pack(pady=10)
        
        ctk.CTkButton(self, text="Entrar", command=lambda: login_callback(self.user.get(), self.senha.get())).pack(pady=20)
        
        # Botão que chama o callback para ir para a tela de cadastro
        ctk.CTkButton(self, text="Não tem conta? Cadastre-se", fg_color="transparent", 
                      text_color="gray", command=ir_para_cadastro_callback).pack()