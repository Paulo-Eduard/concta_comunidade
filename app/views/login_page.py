import customtkinter as ctk

class LoginPage(ctk.CTkFrame):
    def __init__(self, master, login_callback, ir_para_cadastro_callback):
        super().__init__(master, fg_color="transparent")
        # Frame externo que ocupa tudo e centraliza o filho
        outer = ctk.CTkFrame(self, fg_color="transparent")
        outer.pack(fill="both", expand=True)
        # Frame interno é ele que contém os widgets visíveis
        center = ctk.CTkFrame(outer, fg_color="transparent")
        
        center.place(relx=0.5, rely=0.5, anchor="center")

        ctk.CTkLabel(center, text="Bem-vindo ao Conecta", 
                    font=("Arial", 24, "bold")).pack(pady=40)
        self.user = ctk.CTkEntry(center, placeholder_text="Usuário", width=300)
        self.user.pack(pady=10)
        
        self.senha = ctk.CTkEntry(center, placeholder_text="Senha", width=300, show="*")
        self.senha.pack(pady=10)
        
        ctk.CTkButton(center, text="Entrar",
                      command=lambda: login_callback(self.user.get(), self.senha.get())).pack(pady=20)
        
        ctk.CTkButton(center, text="Não tem conta? Cadastre-se",
                      fg_color="transparent", text_color="gray",
                      command=ir_para_cadastro_callback).pack()