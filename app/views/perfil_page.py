import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image

class PerfilPage(ctk.CTkFrame):
    # ADICIONEI logout_callback NOS ARGUMENTOS
    def __init__(self, master, usuario_logado, voltar_callback, logout_callback, db):
        super().__init__(master, fg_color="transparent")
        self.db = db
        self.usuario = usuario_logado
        
        # 1. Botão Voltar
        ctk.CTkButton(self, text="⬅ Voltar", width=100, command=voltar_callback).pack(anchor="nw", padx=20, pady=20)
        
        # 2. Área da Foto
        self.lbl_foto = ctk.CTkLabel(self, text="Sem foto", width=150, height=150, fg_color="#333", corner_radius=75)
        self.lbl_foto.pack(pady=20)
        
        # 3. Título e Dados
        ctk.CTkLabel(self, text="Perfil do Usuário", font=("Arial", 24, "bold")).pack(pady=10)
        
        nome = self.usuario.get('nome', 'Usuário')
        tipo = self.usuario.get('tipo', 'Aluno')
        ctk.CTkLabel(self, text=f"Nome: {nome}", font=("Arial", 16)).pack(pady=5)
        ctk.CTkLabel(self, text=f"Tipo: {tipo.capitalize()}", font=("Arial", 16)).pack(pady=5)
        
        # 4. Botões (Alterar Foto e Sair)
        ctk.CTkButton(self, text="Alterar Foto", command=self.selecionar_foto).pack(pady=10)
        
        # BOTÃO SAIR (Agora com a referência correta do callback)
        ctk.CTkButton(self, text="Sair da Conta", fg_color="red", hover_color="darkred", 
                      command=logout_callback).pack(pady=10)
        
        # Carrega a foto
        try:
            caminho_salvo = self.db.obter_foto_path(self.usuario['username'])
            if caminho_salvo:
                self.exibir_foto(caminho_salvo)
        except:
            pass

    def exibir_foto(self, caminho):
        try:
            img = ctk.CTkImage(light_image=Image.open(caminho), size=(150, 150))
            self.lbl_foto.configure(image=img, text="")
        except:
            self.lbl_foto.configure(text="Erro ao carregar imagem")

    def selecionar_foto(self):
        caminho = filedialog.askopenfilename(filetypes=[("Imagens", "*.png;*.jpg;*.jpeg")])
        if caminho:
            self.db.salvar_foto_path(self.usuario['username'], caminho)
            self.exibir_foto(caminho)