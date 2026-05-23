import customtkinter as ctk


class SegurancaPage(ctk.CTkFrame):

    def __init__(self, master, mudar_pagina_callback, usuario_logado, db):
        super().__init__(master)

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

        voltar = ctk.CTkButton(
            header,
            text="⬅ Voltar",
            width=120,
            height=40,
            fg_color="#2563eb",
            hover_color="#1d4ed8",
            command=lambda:
            mudar_pagina_callback("home")
        )

        voltar.pack(side="left", padx=20)

        titulo = ctk.CTkLabel(
            header,
            text="🔒 Segurança Digital",
            font=("Arial", 28, "bold"),
            text_color="white"
        )

        titulo.pack(side="left", padx=20)

        # =====================================================
        # CONTAINER
        # =====================================================

        scroll = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent"
        )

        scroll.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=25
        )

        dicas = [

            (
                "🔑 Senhas Fortes",
                "Utilize letras maiúsculas, números e símbolos."
            ),

            (
                "📧 Cuidado com Phishing",
                "Nunca clique em links suspeitos."
            ),

            (
                "🛡 Autenticação 2FA",
                "Ative verificação em duas etapas."
            ),

            (
                "💻 Atualizações",
                "Mantenha o sistema sempre atualizado."
            ),

            (
                "📱 Redes Sociais",
                "Não compartilhe informações pessoais."
            )

        ]

        for titulo_dica, texto_dica in dicas:

            card = ctk.CTkFrame(
                scroll,
                fg_color="#111827",
                corner_radius=20
            )

            card.pack(fill="x", pady=15)

            titulo_card = ctk.CTkLabel(
                card,
                text=titulo_dica,
                font=("Arial", 24, "bold")
            )

            titulo_card.pack(
                anchor="w",
                padx=25,
                pady=(20, 10)
            )

            texto = ctk.CTkLabel(
                card,
                text=texto_dica,
                font=("Arial", 16),
                justify="left",
                wraplength=900,
                text_color="#cbd5e1"
            )

            texto.pack(
                anchor="w",
                padx=25,
                pady=(0, 25)
            )