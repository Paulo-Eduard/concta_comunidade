import customtkinter as ctk
from tkinter import filedialog, messagebox
import os

class SegurancaPage(ctk.CTkFrame):
    def __init__(self, master, voltar_callback, usuario_logado, db):
        super().__init__(master, fg_color="transparent")
        self.db = db
        self.usuario = usuario_logado
        self.caminho_arquivo = ""
        
        ctk.CTkButton(self, text="⬅ Voltar", width=100, fg_color="#2d6a9f", command=voltar_callback).pack(anchor="nw", padx=20, pady=20)
        ctk.CTkLabel(self, text="Segurança Digital", font=("Arial", 24, "bold")).pack(pady=10)

        if self.usuario.get('tipo') == 'professor':
            self.criar_painel_professor()
        else:
            self.criar_painel_aluno()

    def criar_painel_professor(self):
        self.entry_titulo = ctk.CTkEntry(self, placeholder_text="Título do Assunto", width=400)
        self.entry_titulo.pack(pady=5)
        
        self.textbox_conteudo = ctk.CTkTextbox(self, width=400, height=200)
        self.textbox_conteudo.pack(pady=5)
        
        ctk.CTkButton(self, text="Anexar Slide/Imagem", command=self.selecionar_arquivo).pack(pady=5)
        ctk.CTkButton(self, text="Publicar Aula", fg_color="green", command=self.salvar_conteudo).pack(pady=10)

    def selecionar_arquivo(self):
        self.caminho_arquivo = filedialog.askopenfilename(filetypes=[("Arquivos", "*.pdf;*.pptx;*.png;*.jpg")])

    def salvar_conteudo(self):
        self.db.salvar_conteudo_seguranca(
            self.entry_titulo.get(), 
            self.textbox_conteudo.get("1.0", "end-1c"), 
            self.caminho_arquivo
        )
        messagebox.showinfo("Sucesso", "Aula publicada!")

    def criar_painel_aluno(self):
        conteudo = self.db.obter_conteudo_seguranca()
        if conteudo:
            ctk.CTkLabel(self, text=conteudo[1], font=("Arial", 20, "bold")).pack(pady=10)
            ctk.CTkLabel(self, text=conteudo[2], wraplength=500).pack(pady=10)
            if conteudo[3]:
                ctk.CTkButton(self, text="Abrir Material de Apoio", command=lambda: os.startfile(conteudo[3])).pack(pady=10)
        else:
            ctk.CTkLabel(self, text="Nenhum conteúdo disponível.").pack(pady=20)