import customtkinter as ctk
from tkinter import messagebox


class RegisterPage(ctk.CTkFrame):

    def __init__(
        self,
        master,
        cadastro_callback,
        voltar_callback
    ):

        super().__init__(master)

        self.cadastro_callback = cadastro_callback
        self.voltar_callback = voltar_callback

        self.configure(
            fg_color="#0f172a"
        )

        container = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        container.pack(
            fill="both",
            expand=True
        )

        self.left = ctk.CTkFrame(
            container,
            fg_color="#111827",
            corner_radius=0
        )

        self.left.place(
            relx=0,
            rely=0,
            relwidth=0.45,
            relheight=1
        )

        left_content = ctk.CTkFrame(
            self.left,
            fg_color="transparent"
        )

        left_content.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        logo = ctk.CTkLabel(
            left_content,
            text="🌐 Conecta\nComunidade",
            font=("Arial", 36, "bold"),
            justify="left",
            text_color="white"
        )

        logo.pack(
            anchor="w",
            pady=(0, 20)
        )

        desc = ctk.CTkLabel(
            left_content,
            text=(
                "Crie sua conta e participe\n"
                "da plataforma de inclusão\n"
                "digital e aprendizado."
            ),
            justify="left",
            font=("Arial", 16),
            text_color="#94a3b8"
        )

        desc.pack(
            anchor="w",
            pady=(0, 25)
        )

        vantagens = [

            "📚 Cursos gratuitos",

            "🧠 Quiz interativo",

            "🤖 Assistente IA",

            "🏆 Certificados",

            "💬 Comunidade"
        ]

        for item in vantagens:

            linha = ctk.CTkLabel(
                left_content,
                text=item,
                font=("Arial", 15),
                text_color="#cbd5e1"
            )

            linha.pack(
                anchor="w",
                pady=6
            )

        self.right = ctk.CTkFrame(
            container,
            fg_color="#0f172a",
            corner_radius=0
        )

        self.right.place(
            relx=0.45,
            rely=0,
            relwidth=0.55,
            relheight=1
        )

        form = ctk.CTkFrame(
            self.right,
            width=620,
            fg_color="#111827",
            corner_radius=25
        )

        form.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        titulo = ctk.CTkLabel(
            form,
            text="📝 Criar Conta",
            font=("Arial", 30, "bold"),
            text_color="white"
        )

        titulo.pack(
            pady=(30, 10)
        )

        subtitulo = ctk.CTkLabel(
            form,
            text="Preencha seus dados abaixo",
            font=("Arial", 14),
            text_color="#94a3b8"
        )

        subtitulo.pack(
            pady=(0, 25)
        )

        self.nome = self.criar_entry(
            form,
            "Nome completo"
        )

        self.username = self.criar_entry(
            form,
            "Usuário"
        )

        self.email = self.criar_entry(
            form,
            "E-mail"
        )

        self.telefone = self.criar_entry(
            form,
            "Telefone"
        )

        self.senha = self.criar_entry(
            form,
            "Senha",
            show="*"
        )

        self.confirmar = self.criar_entry(
            form,
            "Confirmar senha",
            show="*"
        )

        tipo_frame = ctk.CTkFrame(
            form,
            fg_color="transparent"
        )

        tipo_frame.pack(
            fill="x",
            padx=45,
            pady=(10, 15)
        )

        tipo_label = ctk.CTkLabel(
            tipo_frame,
            text="Tipo de conta:",
            font=("Arial", 15, "bold")
        )

        tipo_label.pack(
            anchor="w",
            pady=(0, 8)
        )

        self.tipo = ctk.CTkOptionMenu(
            tipo_frame,
            values=[
                "aluno",
                "professor"
            ],
            height=42,
            fg_color="#2563eb",
            button_color="#1d4ed8",
            dropdown_fg_color="#111827",
            dropdown_hover_color="#2563eb",
            command=self.alterar_tipo
        )

        self.tipo.pack(
            fill="x"
        )

        self.admin_entry = ctk.CTkEntry(
            form,
            placeholder_text="Código administrador",
            height=55,
            corner_radius=12,
            font=("Arial", 14),
            fg_color="#1e293b",
            border_color="#334155",
            text_color="white",
            placeholder_text_color="#64748b",
            show="*"
        )

        cadastrar = ctk.CTkButton(
            form,
            text="🚀 Criar Conta",
            height=48,
            fg_color="#2563eb",
            hover_color="#1d4ed8",
            font=("Arial", 16, "bold"),
            corner_radius=12,
            command=self.fazer_cadastro
        )

        cadastrar.pack(
            fill="x",
            padx=40,
            pady=(10, 15)
        )

        voltar = ctk.CTkButton(
            form,
            text="⬅ Voltar para Login",
            height=42,
            fg_color="transparent",
            hover_color="#1e293b",
            border_width=1,
            border_color="#334155",
            font=("Arial", 14),
            command=self.voltar_callback
        )

        voltar.pack(
            fill="x",
            padx=40,
            pady=(0, 30)
        )

    def alterar_tipo(self, valor):

        if valor == "professor":

            self.admin_entry.pack(
                fill="x",
                padx=40,
                pady=8
            )

        else:

            self.admin_entry.pack_forget()

    def criar_entry(
        self,
        parent,
        placeholder,
        show=None
    ):

        entry = ctk.CTkEntry(
            parent,
            placeholder_text=placeholder,
            height=45,
            corner_radius=12,
            font=("Arial", 14),
            fg_color="#1e293b",
            border_color="#334155",
            text_color="white",
            placeholder_text_color="#64748b",
            show=show
        )

        entry.pack(
            fill="x",
            padx=40,
            pady=8
        )

        return entry

    def fazer_cadastro(self):

        nome = self.nome.get().strip()

        username = self.username.get().strip()

        email = self.email.get().strip()

        telefone = self.telefone.get().strip()

        senha = self.senha.get().strip()

        confirmar = self.confirmar.get().strip()

        tipo = self.tipo.get()

        codigo_admin = self.admin_entry.get().strip()

        if (
            not nome or
            not username or
            not email or
            not telefone or
            not senha or
            not confirmar
        ):

            messagebox.showwarning(
                "Campos vazios",
                "Preencha todos os campos."
            )

            return

        if "@" not in email:

            messagebox.showerror(
                "Email inválido",
                "O email precisa conter @"
            )

            return

        emails_validos = [

            "@gmail.com",

            "@hotmail.com",

            "@outlook.com",

            "@yahoo.com"
        ]

        if not any(
            email.endswith(dominio)
            for dominio in emails_validos
        ):

            messagebox.showerror(
                "Email inválido",
                "Digite um email válido."
            )

            return

        if len(senha) < 4:

            messagebox.showwarning(
                "Senha fraca",
                "A senha precisa ter pelo menos 4 caracteres."
            )

            return

        if senha != confirmar:

            messagebox.showerror(
                "Erro",
                "As senhas não coincidem."
            )

            return

        if tipo == "professor":

            if codigo_admin != "1945":

                messagebox.showerror(
                    "Acesso negado",
                    "Código administrador incorreto."
                )

                return

        self.cadastro_callback(
            username,
            senha,
            nome,
            email,
            telefone,
            tipo
        )
