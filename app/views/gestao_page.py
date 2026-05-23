import customtkinter as ctk
from tkinter import messagebox

class GestaoPage(ctk.CTkFrame):
    def __init__(self, master, mudar_pagina_callback, db):
        super().__init__(master)
        self.mudar_pagina = mudar_pagina_callback
        self.db = db
        self.configure(fg_color="#0f172a")

        container = ctk.CTkScrollableFrame(self, fg_color="transparent")
        container.pack(fill="both", expand=True, padx=25, pady=25)

        ctk.CTkLabel(container, text="⚙ Painel de Gestão", font=("Arial", 28, "bold")).pack(anchor="w")
        ctk.CTkButton(container, text="⬅ Voltar", fg_color="#334155", command=lambda: self.mudar_pagina("home")).pack(anchor="w", pady=20)

        self.exibir_usuarios(container)

    def exibir_usuarios(self, container):
        # Busca os usuários no banco de dados
        usuarios = self.db.buscar_todos_usuarios()
        
        if not usuarios:
            ctk.CTkLabel(container, text="Nenhum usuário cadastrado.").pack(anchor="w")
            return

        for u in usuarios:
            # u[0] = ID, u[1] = Username, u[2] = Nome
            card = ctk.CTkFrame(container, fg_color="#1e293b")
            card.pack(fill="x", pady=5, padx=5)

            info = ctk.CTkLabel(card, text=f"Nome: {u[2]} | Usuário: {u[1]}", anchor="w")
            info.pack(side="left", padx=15, pady=15, fill="x", expand=True)

            # Botão de Excluir com confirmação
            btn_excluir = ctk.CTkButton(
                card, 
                text="Excluir", 
                fg_color="#ef4444", 
                hover_color="#b91c1c",
                width=80,
                command=lambda uid=u[0]: self.confirmar_exclusao(uid)
            )
            btn_excluir.pack(side="right", padx=15)

    def confirmar_exclusao(self, usuario_id):
        # Janela de notificação para confirmar a exclusão
        resposta = messagebox.askyesno(
            "Confirmar Exclusão", 
            "Tem certeza que deseja excluir este usuário? Esta ação não pode ser desfeita."
        )
        
        if resposta: # Se clicar em 'Sim'
            self.db.excluir_usuario(usuario_id)
            # Recarrega a página para atualizar a lista automaticamente
            self.mudar_pagina("gestao")