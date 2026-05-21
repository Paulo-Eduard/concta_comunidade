import customtkinter as ctk
from tkinter import messagebox

class CursosPage(ctk.CTkFrame):
    def __init__(self, master, voltar_callback, usuario_logado, db):
        super().__init__(master, fg_color="transparent")
        self.db = db
        self.usuario = usuario_logado
        
        ctk.CTkButton(self, text="⬅ Voltar", command=voltar_callback).pack(anchor="nw", padx=20, pady=20)
        
        if self.usuario.get('tipo') == 'professor':
            self.criar_painel_professor()
        else:
            self.criar_painel_aluno()

    # --- Lógica do Professor ---
    def criar_painel_professor(self):
        self.entry_titulo = ctk.CTkEntry(self, placeholder_text="Título do Módulo", width=300)
        self.entry_titulo.pack(pady=10)
        self.textbox_conteudo = ctk.CTkTextbox(self, width=300, height=100)
        self.textbox_conteudo.pack(pady=10)
        ctk.CTkButton(self, text="Adicionar Módulo", command=self.salvar_modulo).pack(pady=10)
        
        ctk.CTkLabel(self, text="Módulos Cadastrados:", font=("Arial", 14, "bold")).pack(pady=10)
        self.lista_modulos_prof()

    def lista_modulos_prof(self):
        # Limpa a lista atual para não duplicar ao recarregar
        for widget in self.winfo_children():
            if isinstance(widget, ctk.CTkFrame) and widget != self.winfo_children()[0]:
                widget.destroy()
        
        modulos = self.db.obter_modulos()
        for m in modulos:
            frame = ctk.CTkFrame(self)
            frame.pack(fill="x", padx=20, pady=5)
            ctk.CTkLabel(frame, text=m[1]).pack(side="left", padx=10)
            ctk.CTkButton(frame, text="Excluir", fg_color="red", command=lambda id=m[0]: self.deletar_modulo(id)).pack(side="right", padx=10)

    def salvar_modulo(self):
        self.db.adicionar_modulo(self.entry_titulo.get(), self.textbox_conteudo.get("1.0", "end-1c"))
        messagebox.showinfo("Sucesso", "Módulo adicionado!")
        self.lista_modulos_prof()

    def deletar_modulo(self, id):
        self.db.excluir_modulo(id)
        messagebox.showinfo("Sucesso", "Módulo removido!")
        self.lista_modulos_prof()

    # --- Lógica do Aluno ---
    def criar_painel_aluno(self):
        modulos = self.db.obter_modulos()
        concluidos = self.db.obter_progresso(self.usuario['id'])
        
        # Barra de Progresso
        total = len(modulos)
        prog_valor = len(concluidos) / total if total > 0 else 0
        
        ctk.CTkLabel(self, text="Progresso do Curso:").pack(pady=5)
        self.barra = ctk.CTkProgressBar(self, width=300)
        self.barra.pack(pady=5)
        self.barra.set(prog_valor)
        
        for m in modulos:
            status = "✅" if m[0] in concluidos else "⚪"
            frame = ctk.CTkFrame(self)
            frame.pack(fill="x", padx=20, pady=5)
            ctk.CTkLabel(frame, text=f"{status} {m[1]}").pack(side="left", padx=10)
            ctk.CTkButton(frame, text="Ver/Concluir", command=lambda m_id=m[0], cont=m[2]: self.abrir_e_concluir(m_id, cont)).pack(side="right", padx=10)

        # Lógica do Certificado
        if total > 0 and len(concluidos) == total:
            ctk.CTkButton(self, text="Baixar Certificado", fg_color="gold", text_color="black", 
                          command=self.emitir_certificado).pack(pady=20)
        else:
            ctk.CTkLabel(self, text="Complete todos os módulos para liberar o certificado.").pack(pady=5)

    def abrir_e_concluir(self, m_id, conteudo):
        messagebox.showinfo("Conteúdo", conteudo)
        self.db.marcar_modulo_concluido(self.usuario['id'], m_id)
        messagebox.showinfo("Sucesso", "Progresso salvo! A tela será atualizada.")
        # Atualiza a página para mostrar o check verde
        self.limpar_interface_aluno()
        self.criar_painel_aluno()

    def limpar_interface_aluno(self):
        for widget in self.winfo_children():
            if widget != self.winfo_children()[0]: # Mantém o botão voltar
                widget.destroy()

    def emitir_certificado(self):
        messagebox.showinfo("Parabéns!", f"Certificado emitido com sucesso para: {self.usuario['nome']}")