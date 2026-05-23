import customtkinter as ctk
from tkinter import messagebox


class ChatPage(ctk.CTkFrame):

    def __init__(self, master, mudar_pagina_callback, usuario_logado, db):
        super().__init__(master)

        self.db = db
        self.usuario = usuario_logado
        self.mudar_pagina = mudar_pagina_callback

        self.configure(fg_color="#0f172a")

        # =====================================================
        # HEADER
        # =====================================================

        self.header = ctk.CTkFrame(
            self,
            height=80,
            fg_color="#111827",
            corner_radius=0
        )

        self.header.pack(fill="x")
        self.header.pack_propagate(False)

        btn_voltar = ctk.CTkButton(
            self.header,
            text="⬅ Voltar",
            width=120,
            height=40,
            fg_color="#2563eb",
            hover_color="#1d4ed8",
            font=("Arial", 14, "bold"),
            command=lambda: self.mudar_pagina("home")
        )

        btn_voltar.pack(side="left", padx=20)

        titulo = ctk.CTkLabel(
            self.header,
            text="💬 Chat da Comunidade",
            font=("Arial", 28, "bold"),
            text_color="white"
        )

        titulo.pack(side="left", padx=20)

        usuario_nome = self.usuario.get("nome", "Usuário")

        perfil = ctk.CTkLabel(
            self.header,
            text=f"👤 {usuario_nome}",
            font=("Arial", 15),
            text_color="#cbd5e1"
        )

        perfil.pack(side="right", padx=25)

        # =====================================================
        # CONTAINER
        # =====================================================

        self.main = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.main.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=25
        )

        # =====================================================
        # ÁREA DE MENSAGENS
        # =====================================================

        self.chat_box = ctk.CTkScrollableFrame(
            self.main,
            fg_color="#111827",
            corner_radius=20
        )

        self.chat_box.pack(
            fill="both",
            expand=True,
            pady=(0, 20)
        )

        # =====================================================
        # ÁREA DE ENVIO
        # =====================================================

        bottom = ctk.CTkFrame(
            self.main,
            fg_color="transparent"
        )

        bottom.pack(fill="x")

        self.entry_msg = ctk.CTkEntry(
            bottom,
            placeholder_text="Digite sua mensagem...",
            height=50,
            font=("Arial", 15),
            corner_radius=12
        )

        self.entry_msg.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(0, 15)
        )

        btn_enviar = ctk.CTkButton(
            bottom,
            text="📤 Enviar",
            width=160,
            height=50,
            fg_color="#2563eb",
            hover_color="#1d4ed8",
            font=("Arial", 15, "bold"),
            corner_radius=12,
            command=self.enviar_mensagem
        )

        btn_enviar.pack(side="right")

        # =====================================================
        # CARREGAR MENSAGENS
        # =====================================================

        self.carregar_mensagens()

    # =====================================================
    # CARREGAR CHAT
    # =====================================================

    def carregar_mensagens(self):

        for widget in self.chat_box.winfo_children():
            widget.destroy()

        mensagens = self.db.obter_mensagens()

        if not mensagens:

            vazio = ctk.CTkLabel(
                self.chat_box,
                text="Nenhuma mensagem ainda.",
                font=("Arial", 18),
                text_color="#94a3b8"
            )

            vazio.pack(pady=40)

            return

        for nome, mensagem in mensagens:

            card = ctk.CTkFrame(
                self.chat_box,
                fg_color="#1e293b",
                corner_radius=18
            )

            card.pack(
                fill="x",
                padx=15,
                pady=10
            )

            usuario = ctk.CTkLabel(
                card,
                text=f"👤 {nome}",
                font=("Arial", 16, "bold"),
                text_color="#60a5fa"
            )

            usuario.pack(
                anchor="w",
                padx=18,
                pady=(15, 5)
            )

            texto = ctk.CTkLabel(
                card,
                text=mensagem,
                font=("Arial", 15),
                justify="left",
                wraplength=850,
                text_color="#e2e8f0"
            )

            texto.pack(
                anchor="w",
                padx=18,
                pady=(0, 15)
            )

    # =====================================================
    # ENVIAR
    # =====================================================

    def enviar_mensagem(self):

        mensagem = self.entry_msg.get().strip()

        if not mensagem:

            messagebox.showwarning(
                "Campo vazio",
                "Digite uma mensagem."
            )

            return

        self.db.enviar_mensagem(
            self.usuario["id"],
            mensagem
        )

        self.entry_msg.delete(0, "end")

        self.carregar_mensagens()