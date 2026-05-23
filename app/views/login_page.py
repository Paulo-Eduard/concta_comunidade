import customtkinter as ctk


class LoginPage(ctk.CTkFrame):

    def __init__(
        self,
        master,
        login_callback,
        ir_para_cadastro_callback
    ):

        super().__init__(
            master,
            fg_color="transparent"
        )

        # =====================================================
        # FRAME PRINCIPAL
        # =====================================================

        outer = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        outer.pack(
            fill="both",
            expand=True
        )

        # =====================================================
        # LADO ESQUERDO
        # =====================================================

        self.left = ctk.CTkFrame(
            outer,
            fg_color="#1e3a5f",
            corner_radius=0
        )

        self.left.place(
            relx=0,
            rely=0,
            relwidth=0.45,
            relheight=1
        )

        left_inner = ctk.CTkFrame(
            self.left,
            fg_color="transparent"
        )

        left_inner.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        # =====================================================
        # LOGO / TÍTULO
        # =====================================================

        logo = ctk.CTkLabel(
            left_inner,
            text="🌐",
            font=("Arial", 70)
        )

        logo.pack(pady=(0, 10))

        titulo = ctk.CTkLabel(
            left_inner,
            text="Conecta Comunidade",
            font=("Arial", 28, "bold"),
            text_color="white"
        )

        titulo.pack()

        subtitulo = ctk.CTkLabel(
            left_inner,
            text=(
                "Aprenda, evolua e conecte-se\n"
                "com sua comunidade."
            ),
            font=("Arial", 15),
            text_color="#cbd5e1",
            justify="left"
        )

        subtitulo.pack(
            pady=(10, 30)
        )

        # =====================================================
        # BENEFÍCIOS
        # =====================================================

        beneficios = [

            ("📚", "Cursos interativos"),

            ("🛡️", "Segurança digital"),

            ("🤖", "Chatbot com IA"),

            ("🏆", "Sistema de progresso"),

            ("🌍", "Inclusão tecnológica")
        ]

        for icone, texto in beneficios:

            row = ctk.CTkFrame(
                left_inner,
                fg_color="transparent"
            )

            row.pack(
                anchor="w",
                pady=6
            )

            ctk.CTkLabel(
                row,
                text=icone,
                font=("Arial", 16)
            ).pack(side="left")

            ctk.CTkLabel(
                row,
                text=f"  {texto}",
                font=("Arial", 14),
                text_color="#e2e8f0"
            ).pack(side="left")

        # =====================================================
        # LADO DIREITO
        # =====================================================

        self.right = ctk.CTkFrame(
            outer,
            fg_color="#0f172a",
            corner_radius=0
        )

        self.right.place(
            relx=0.45,
            rely=0,
            relwidth=0.55,
            relheight=1
        )

        right_inner = ctk.CTkFrame(
            self.right,
            width=420,
            height=480,
            corner_radius=20,
            fg_color="#111827",
            border_width=1,
            border_color="#1e293b"
        )

        right_inner.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        # =====================================================
        # TÍTULO LOGIN
        # =====================================================

        login_titulo = ctk.CTkLabel(
            right_inner,
            text="Acesse sua conta",
            font=("Arial", 28, "bold"),
            text_color="white"
        )

        login_titulo.pack(
            pady=(40, 10)
        )

        login_desc = ctk.CTkLabel(
            right_inner,
            text="Entre para continuar sua jornada",
            font=("Arial", 14),
            text_color="#94a3b8"
        )

        login_desc.pack(
            pady=(0, 30)
        )

        # =====================================================
        # CAMPO USUÁRIO
        # =====================================================

        self.user = ctk.CTkEntry(

            right_inner,

            placeholder_text="Usuário",

            width=320,

            height=45,

            corner_radius=12,

            fg_color="#1e293b",

            border_color="#334155",

            text_color="white",

            placeholder_text_color="#94a3b8",

            font=("Arial", 14)
        )

        self.user.pack(
            pady=(0, 15)
        )

        # =====================================================
        # CAMPO SENHA
        # =====================================================

        self.senha = ctk.CTkEntry(

            right_inner,

            placeholder_text="Senha",

            width=320,

            height=45,

            show="*",

            corner_radius=12,

            fg_color="#1e293b",

            border_color="#334155",

            text_color="white",

            placeholder_text_color="#94a3b8",

            font=("Arial", 14)
        )

        self.senha.pack(
            pady=(0, 20)
        )

        # =====================================================
        # ENTER PARA LOGAR
        # =====================================================

        self.senha.bind(
            "<Return>",
            lambda e:
            login_callback(
                self.user.get(),
                self.senha.get()
            )
        )

        # =====================================================
        # BOTÃO LOGIN
        # =====================================================

        btn_login = ctk.CTkButton(

            right_inner,

            text="Entrar",

            width=320,

            height=45,

            corner_radius=12,

            fg_color="#2563eb",

            hover_color="#1d4ed8",

            font=("Arial", 15, "bold"),

            command=lambda:
            login_callback(
                self.user.get(),
                self.senha.get()
            )
        )

        btn_login.pack(
            pady=(5, 20)
        )

        # =====================================================
        # DIVISOR
        # =====================================================

        divisor = ctk.CTkLabel(
            right_inner,
            text="──────── ou ────────",
            text_color="#475569",
            font=("Arial", 12)
        )

        divisor.pack(
            pady=10
        )

        # =====================================================
        # BOTÃO CADASTRO
        # =====================================================

        btn_cadastro = ctk.CTkButton(

            right_inner,

            text="Criar nova conta",

            width=320,

            height=42,

            corner_radius=12,

            fg_color="transparent",

            border_width=1,

            border_color="#334155",

            hover_color="#1e293b",

            text_color="#cbd5e1",

            font=("Arial", 14),

            command=ir_para_cadastro_callback
        )

        btn_cadastro.pack(
            pady=(10, 30)
        )

        # =====================================================
        # RODAPÉ
        # =====================================================

        footer = ctk.CTkLabel(
            right_inner,
            text="© 2026 Conecta Comunidade",
            text_color="#475569",
            font=("Arial", 11)
        )

        footer.pack(
            pady=(10, 20)
        )