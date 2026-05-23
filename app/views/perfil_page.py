import customtkinter as ctk
from tkinter import messagebox, filedialog
from PIL import Image


class PerfilPage(ctk.CTkFrame):

    def __init__(self, master, usuario_logado, mudar_pagina_callback, logout_callback, db):
        super().__init__(master)

        self.usuario = usuario_logado
        self.db = db
        self.mudar_pagina = mudar_pagina_callback
        self.logout = logout_callback

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
            text="👤 Meu Perfil",
            font=("Arial", 28, "bold"),
            text_color="white"
        )

        titulo.pack(side="left", padx=20)

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
            padx=30,
            pady=30
        )

        # =====================================================
        # CARD PERFIL
        # =====================================================

        self.card = ctk.CTkFrame(
            self.main,
            fg_color="#111827",
            corner_radius=25
        )

        self.card.pack(
            expand=True,
            fill="both"
        )

        # =====================================================
        # FOTO
        # =====================================================

        self.foto_label = ctk.CTkLabel(
            self.card,
            text=""
        )

        self.foto_label.pack(pady=(35, 15))

        self.carregar_foto()

        btn_foto = ctk.CTkButton(
            self.card,
            text="🖼 Alterar Foto",
            width=180,
            height=42,
            fg_color="#2563eb",
            hover_color="#1d4ed8",
            font=("Arial", 14, "bold"),
            command=self.alterar_foto
        )

        btn_foto.pack(pady=(0, 30))

        # =====================================================
        # DADOS
        # =====================================================

        nome = self.usuario.get("nome", "Usuário")

        tipo = self.usuario.get("tipo", "aluno").capitalize()

        username = self.usuario.get("username", "Sem username")

        titulo_nome = ctk.CTkLabel(
            self.card,
            text=nome,
            font=("Arial", 30, "bold"),
            text_color="white"
        )

        titulo_nome.pack(pady=(0, 8))

        cargo = ctk.CTkLabel(
            self.card,
            text=f"🎓 {tipo}",
            font=("Arial", 18),
            text_color="#60a5fa"
        )

        cargo.pack()

        user_label = ctk.CTkLabel(
            self.card,
            text=f"@{username}",
            font=("Arial", 15),
            text_color="#94a3b8"
        )

        user_label.pack(pady=(5, 25))

        # =====================================================
        # ESTATÍSTICAS
        # =====================================================

        stats_frame = ctk.CTkFrame(
            self.card,
            fg_color="transparent"
        )

        stats_frame.pack(pady=15)

        stats = [
            ("📚 Cursos", "12"),
            ("🧠 Quiz", "8"),
            ("🏆 Nível", "Intermediário")
        ]

        for titulo_stat, valor in stats:

            box = ctk.CTkFrame(
                stats_frame,
                fg_color="#1e293b",
                width=180,
                height=110,
                corner_radius=18
            )

            box.pack(side="left", padx=15)
            box.pack_propagate(False)

            valor_label = ctk.CTkLabel(
                box,
                text=valor,
                font=("Arial", 24, "bold"),
                text_color="#60a5fa"
            )

            valor_label.pack(pady=(22, 6))

            titulo_label = ctk.CTkLabel(
                box,
                text=titulo_stat,
                font=("Arial", 14),
                text_color="#cbd5e1"
            )

            titulo_label.pack()

        # =====================================================
        # BOTÕES
        # =====================================================

        botoes = ctk.CTkFrame(
            self.card,
            fg_color="transparent"
        )

        botoes.pack(pady=35)

        btn_home = ctk.CTkButton(
            botoes,
            text="🏠 Início",
            width=180,
            height=48,
            fg_color="#2563eb",
            hover_color="#1d4ed8",
            font=("Arial", 15, "bold"),
            command=lambda: self.mudar_pagina("home")
        )

        btn_home.pack(side="left", padx=12)

        btn_logout = ctk.CTkButton(
            botoes,
            text="🚪 Sair",
            width=180,
            height=48,
            fg_color="#dc2626",
            hover_color="#b91c1c",
            font=("Arial", 15, "bold"),
            command=self.logout
        )

        btn_logout.pack(side="left", padx=12)

    # =====================================================
    # FOTO
    # =====================================================

    def carregar_foto(self):

        caminho = self.db.obter_foto_path(
            self.usuario["username"]
        )

        try:

            if caminho:

                imagem = ctk.CTkImage(
                    light_image=Image.open(caminho),
                    dark_image=Image.open(caminho),
                    size=(140, 140)
                )

                self.foto_label.configure(
                    image=imagem,
                    text=""
                )

                self.foto_label.image = imagem

            else:

                self.foto_label.configure(
                    text="👤",
                    font=("Arial", 90),
                    text_color="#60a5fa"
                )

        except:

            self.foto_label.configure(
                text="👤",
                font=("Arial", 90),
                text_color="#60a5fa"
            )

    # =====================================================
    # ALTERAR FOTO
    # =====================================================

    def alterar_foto(self):

        caminho = filedialog.askopenfilename(
            title="Selecionar Foto",
            filetypes=[
                ("Imagens", "*.png *.jpg *.jpeg")
            ]
        )

        if not caminho:
            return

        self.db.salvar_foto_path(
            self.usuario["username"],
            caminho
        )

        self.carregar_foto()

        messagebox.showinfo(
            "Sucesso",
            "Foto atualizada!"
        )