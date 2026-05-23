import customtkinter as ctk

class HomePage(ctk.CTkFrame):

    def __init__(self, master, mudar_pagina_callback, usuario_logado, logout_callback):
        super().__init__(master)

        # Proteção: Garante que self.usuario seja um dicionário mesmo se for None
        self.usuario = usuario_logado if usuario_logado is not None else {}
        self.mudar_pagina = mudar_pagina_callback
        self.logout = logout_callback

        self.configure(fg_color="#0f172a")

        # =====================================================
        # HEADER
        # =====================================================

        header = ctk.CTkFrame(
            self,
            height=80,
            fg_color="#111827",
            corner_radius=0
        )

        header.pack(fill="x")
        header.pack_propagate(False)

        titulo = ctk.CTkLabel(
            header,
            text="🌐 Conecta Comunidade",
            font=("Arial", 28, "bold"),
            text_color="white"
        )

        titulo.pack(side="left", padx=25)

        usuario_nome = self.usuario.get("nome", "Usuário")

        perfil = ctk.CTkLabel(
            header,
            text=f"👤 {usuario_nome}",
            font=("Arial", 15),
            text_color="#cbd5e1"
        )

        perfil.pack(side="right", padx=25)

        # =====================================================
        # CONTAINER
        # =====================================================

        main = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent"
        )

        main.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=25
        )

        # =====================================================
        # BEM-VINDO
        # =====================================================

        welcome = ctk.CTkFrame(
            main,
            fg_color="#111827",
            corner_radius=25
        )

        welcome.pack(fill="x", pady=(0, 25))

        texto = ctk.CTkLabel(
            welcome,
            text=f"Bem-vindo, {usuario_nome} 🚀",
            font=("Arial", 32, "bold"),
            text_color="white"
        )

        texto.pack(anchor="w", padx=30, pady=(25, 10))

        subtitulo = ctk.CTkLabel(
            welcome,
            text="Aprenda tecnologia, segurança digital e evolua com a comunidade.",
            font=("Arial", 16),
            text_color="#94a3b8"
        )

        subtitulo.pack(anchor="w", padx=30, pady=(0, 25))

        # =====================================================
        # CARDS
        # =====================================================

        cards = ctk.CTkFrame(
            main,
            fg_color="transparent"
        )

        cards.pack(fill="x")

        itens = [
            ("📚 Cursos", "#2563eb", "cursos"),
            ("🧠 Quiz", "#7c3aed", "quiz"),
            ("🤖 IA", "#0891b2", "chatbot"),
            ("💬 Chat", "#16a34a", "chat"),
            ("🔒 Segurança", "#dc2626", "seguranca"),
            ("👤 Perfil", "#ea580c", "perfil")
        ]

        for i, (titulo_card, cor, destino) in enumerate(itens):

            card = ctk.CTkFrame(
                cards,
                fg_color="#111827",
                corner_radius=22,
                width=260,
                height=170
            )

            row = i // 3
            col = i % 3

            card.grid(
                row=row,
                column=col,
                padx=15,
                pady=15
            )

            card.grid_propagate(False)

            titulo_lbl = ctk.CTkLabel(
                card,
                text=titulo_card,
                font=("Arial", 24, "bold")
            )

            titulo_lbl.pack(pady=(30, 15))

            btn = ctk.CTkButton(
                card,
                text="Acessar",
                width=180,
                height=42,
                fg_color=cor,
                hover_color=cor,
                font=("Arial", 14, "bold"),
                command=lambda d=destino: self.mudar_pagina(d)
            )

            btn.pack()

        # =====================================================
        # ADMIN
        # =====================================================

        if self.usuario.get("tipo") == "professor":

            admin = ctk.CTkFrame(
                main,
                fg_color="#111827",
                corner_radius=25
            )

            admin.pack(fill="x", pady=25)

            titulo_admin = ctk.CTkLabel(
                admin,
                text="⚙ Painel Administrativo",
                font=("Arial", 24, "bold")
            )

            titulo_admin.pack(anchor="w", padx=25, pady=(25, 10))

            btn_admin = ctk.CTkButton(
                admin,
                text="Abrir Gestão",
                width=220,
                height=45,
                fg_color="#2563eb",
                hover_color="#1d4ed8",
                command=lambda: self.mudar_pagina("gestao")
            )

            btn_admin.pack(padx=25, pady=(0, 25))

        # =====================================================
        # LOGOUT
        # =====================================================

        # Proteção: Verifica se o logout existe antes de criar o botão
        if self.logout:
            sair = ctk.CTkButton(
                main,
                text="🚪 Sair da Conta",
                height=48,
                fg_color="#dc2626",
                hover_color="#b91c1c",
                font=("Arial", 15, "bold"),
                command=self.logout
            )

            sair.pack(fill="x", pady=20)