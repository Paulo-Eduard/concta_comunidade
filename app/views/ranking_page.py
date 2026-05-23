import customtkinter as ctk


class RankingPage(ctk.CTkFrame):

    def __init__(
        self,
        master,
        mudar_pagina_callback,
        db
    ):

        super().__init__(master)

        self.db = db
        self.mudar_pagina = mudar_pagina_callback

        self.configure(
            fg_color="#0f172a"
        )

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

            font=("Arial", 14, "bold"),

            command=lambda:
            self.mudar_pagina("home")

        )

        voltar.pack(
            side="left",
            padx=20
        )

        titulo = ctk.CTkLabel(

            header,

            text="🏆 Ranking de Alunos",

            font=("Arial", 28, "bold")

        )

        titulo.pack(
            side="left",
            padx=20
        )

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
        # TOP 3
        # =====================================================

        top_frame = ctk.CTkFrame(
            self.main,
            fg_color="transparent"
        )

        top_frame.pack(
            fill="x",
            pady=(0, 30)
        )

        ranking = self.db.obter_ranking()

        top3 = ranking[:3]

        cores = [
            "#facc15",
            "#94a3b8",
            "#b45309"
        ]

        medalhas = [
            "🥇",
            "🥈",
            "🥉"
        ]

        for i, jogador in enumerate(top3):

            nome = jogador[0]
            nota = jogador[1]

            card = ctk.CTkFrame(

                top_frame,

                fg_color="#111827",

                corner_radius=20,

                width=300,

                height=180

            )

            card.grid(
                row=0,
                column=i,
                padx=15
            )

            card.pack_propagate(False)

            medalha = ctk.CTkLabel(

                card,

                text=medalhas[i],

                font=("Arial", 42)

            )

            medalha.pack(
                pady=(20, 5)
            )

            nome_label = ctk.CTkLabel(

                card,

                text=nome,

                font=("Arial", 22, "bold")

            )

            nome_label.pack()

            nota_label = ctk.CTkLabel(

                card,

                text=f"{nota:.0f}%",

                font=("Arial", 30, "bold"),

                text_color=cores[i]

            )

            nota_label.pack(
                pady=10
            )

        # =====================================================
        # LISTA
        # =====================================================

        lista_frame = ctk.CTkFrame(
            self.main,
            fg_color="#111827",
            corner_radius=20
        )

        lista_frame.pack(
            fill="both",
            expand=True
        )

        titulo_lista = ctk.CTkLabel(

            lista_frame,

            text="📊 Classificação Geral",

            font=("Arial", 24, "bold")

        )

        titulo_lista.pack(
            anchor="w",
            padx=25,
            pady=(20, 10)
        )

        scroll = ctk.CTkScrollableFrame(
            lista_frame,
            fg_color="transparent"
        )

        scroll.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        if not ranking:

            vazio = ctk.CTkLabel(

                scroll,

                text="Nenhum resultado encontrado.",

                font=("Arial", 18)

            )

            vazio.pack(pady=40)

            return

        for posicao, jogador in enumerate(ranking):

            nome = jogador[0]
            nota = jogador[1]

            linha = ctk.CTkFrame(
                scroll,
                fg_color="#1e293b",
                corner_radius=15,
                height=70
            )

            linha.pack(
                fill="x",
                pady=8
            )

            pos = ctk.CTkLabel(

                linha,

                text=f"#{posicao + 1}",

                font=("Arial", 20, "bold"),

                width=80

            )

            pos.pack(
                side="left",
                padx=15
            )

            nome_label = ctk.CTkLabel(

                linha,

                text=nome,

                font=("Arial", 18)

            )

            nome_label.pack(
                side="left"
            )

            nota_label = ctk.CTkLabel(

                linha,

                text=f"{nota:.0f}%",

                font=("Arial", 20, "bold"),

                text_color="#22c55e"

            )

            nota_label.pack(
                side="right",
                padx=20
            )