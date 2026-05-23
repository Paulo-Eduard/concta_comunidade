import customtkinter as ctk
from tkinter import messagebox


class QuizPage(ctk.CTkFrame):

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
            text="🧠 Central de Quiz",
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
        # CONTAINER PRINCIPAL
        # =====================================================

        self.main = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.main.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=25
        )

        if self.usuario.get("tipo") == "professor":
            self.criar_painel_professor()
        else:
            self.criar_painel_aluno()

    # =====================================================
    # PROFESSOR
    # =====================================================

    def criar_painel_professor(self):

        top = ctk.CTkFrame(
            self.main,
            fg_color="#111827",
            corner_radius=20
        )

        top.pack(fill="x", pady=(0, 25))

        titulo = ctk.CTkLabel(
            top,
            text="➕ Criar Nova Questão",
            font=("Arial", 26, "bold")
        )

        titulo.pack(pady=(25, 20))

        # =========================
        # FORM
        # =========================

        self.p = ctk.CTkEntry(
            top,
            placeholder_text="Digite a pergunta...",
            height=45,
            font=("Arial", 14),
            corner_radius=10
        )

        self.p.pack(fill="x", padx=40, pady=8)

        self.a = ctk.CTkEntry(
            top,
            placeholder_text="Alternativa A",
            height=42
        )

        self.a.pack(fill="x", padx=40, pady=8)

        self.b = ctk.CTkEntry(
            top,
            placeholder_text="Alternativa B",
            height=42
        )

        self.b.pack(fill="x", padx=40, pady=8)

        self.c = ctk.CTkEntry(
            top,
            placeholder_text="Alternativa C",
            height=42
        )

        self.c.pack(fill="x", padx=40, pady=8)

        self.d = ctk.CTkEntry(
            top,
            placeholder_text="Alternativa D",
            height=42
        )

        self.d.pack(fill="x", padx=40, pady=8)

        # =========================
        # RESPOSTA CORRETA
        # =========================

        frame_select = ctk.CTkFrame(
            top,
            fg_color="transparent"
        )

        frame_select.pack(pady=15)

        label = ctk.CTkLabel(
            frame_select,
            text="Resposta Correta:",
            font=("Arial", 15, "bold")
        )

        label.pack(side="left", padx=10)

        self.correta = ctk.CTkOptionMenu(
            frame_select,
            values=["A", "B", "C", "D"],
            width=120,
            height=40,
            fg_color="#2563eb",
            button_color="#1d4ed8"
        )

        self.correta.pack(side="left")

        # =========================
        # BOTÃO
        # =========================

        btn_add = ctk.CTkButton(
            top,
            text="🚀 Publicar Questão",
            height=45,
            width=220,
            fg_color="#2563eb",
            hover_color="#1d4ed8",
            font=("Arial", 15, "bold"),
            corner_radius=12,
            command=self.salvar
        )

        btn_add.pack(pady=(10, 25))

        # =====================================================
        # QUESTÕES
        # =====================================================

        titulo_lista = ctk.CTkLabel(
            self.main,
            text="📖 Questões Publicadas",
            font=("Arial", 24, "bold")
        )

        titulo_lista.pack(anchor="w", pady=(5, 15))

        self.lista_scroll = ctk.CTkScrollableFrame(
            self.main,
            fg_color="#111827",
            corner_radius=20
        )

        self.lista_scroll.pack(
            fill="both",
            expand=True
        )

        self.atualizar_lista_perguntas()

    # =====================================================
    # LISTAR QUESTÕES
    # =====================================================

    def atualizar_lista_perguntas(self):

        for w in self.lista_scroll.winfo_children():
            w.destroy()

        perguntas = self.db.obter_perguntas()

        if not perguntas:

            vazio = ctk.CTkLabel(
                self.lista_scroll,
                text="Nenhuma questão cadastrada.",
                font=("Arial", 16)
            )

            vazio.pack(pady=30)

            return

        for q in perguntas:

            card = ctk.CTkFrame(
                self.lista_scroll,
                fg_color="#1e293b",
                corner_radius=18
            )

            card.pack(
                fill="x",
                padx=20,
                pady=10
            )

            pergunta = ctk.CTkLabel(
                card,
                text=q[1],
                font=("Arial", 18, "bold"),
                wraplength=900,
                justify="left"
            )

            pergunta.pack(
                anchor="w",
                padx=20,
                pady=(18, 10)
            )

            correta = ctk.CTkLabel(
                card,
                text=f"✅ Correta: {q[6]}",
                font=("Arial", 14),
                text_color="#22c55e"
            )

            correta.pack(
                anchor="w",
                padx=20,
                pady=(0, 15)
            )

            btn_excluir = ctk.CTkButton(
                card,
                text="🗑 Excluir",
                width=140,
                fg_color="#dc2626",
                hover_color="#b91c1c",
                command=lambda id=q[0]:
                self.deletar_pergunta(id)
            )

            btn_excluir.pack(
                anchor="e",
                padx=20,
                pady=(0, 18)
            )

    # =====================================================
    # SALVAR
    # =====================================================

    def salvar(self):

        pergunta = self.p.get().strip()

        a = self.a.get().strip()
        b = self.b.get().strip()
        c = self.c.get().strip()
        d = self.d.get().strip()

        correta = self.correta.get()

        if not pergunta or not a or not b or not c or not d:

            messagebox.showwarning(
                "Campos vazios",
                "Preencha todos os campos."
            )

            return

        self.db.adicionar_pergunta(
            pergunta,
            a,
            b,
            c,
            d,
            correta
        )

        messagebox.showinfo(
            "Sucesso",
            "Questão publicada!"
        )

        self.p.delete(0, "end")
        self.a.delete(0, "end")
        self.b.delete(0, "end")
        self.c.delete(0, "end")
        self.d.delete(0, "end")

        self.atualizar_lista_perguntas()

    # =====================================================
    # EXCLUIR
    # =====================================================

    def deletar_pergunta(self, pergunta_id):

        confirmar = messagebox.askyesno(
            "Excluir",
            "Deseja excluir esta questão?"
        )

        if confirmar:

            self.db.excluir_pergunta(pergunta_id)

            messagebox.showinfo(
                "Sucesso",
                "Questão removida!"
            )

            self.atualizar_lista_perguntas()

    # =====================================================
    # ALUNO
    # =====================================================

    def criar_painel_aluno(self):

        self.perguntas = self.db.obter_perguntas()

        if not self.perguntas:

            vazio = ctk.CTkLabel(
                self.main,
                text="Nenhuma pergunta disponível.",
                font=("Arial", 20)
            )

            vazio.pack(pady=50)

            return

        self.index = 0
        self.pontos = 0

        self.quiz_frame = ctk.CTkFrame(
            self.main,
            fg_color="#111827",
            corner_radius=20
        )

        self.quiz_frame.pack(
            fill="both",
            expand=True
        )

        self.mostrar_pergunta()

    # =====================================================
    # MOSTRAR
    # =====================================================

    def mostrar_pergunta(self):

        for w in self.quiz_frame.winfo_children():
            w.destroy()

        q = self.perguntas[self.index]

        pergunta = ctk.CTkLabel(
            self.quiz_frame,
            text=q[1],
            font=("Arial", 24, "bold"),
            wraplength=900,
            justify="center"
        )

        pergunta.pack(
            pady=(40, 30),
            padx=30
        )

        alternativas = [
            ("A", q[2]),
            ("B", q[3]),
            ("C", q[4]),
            ("D", q[5])
        ]

        for letra, texto in alternativas:

            btn = ctk.CTkButton(
                self.quiz_frame,
                text=f"{letra}) {texto}",
                height=50,
                font=("Arial", 16),
                fg_color="#1e293b",
                hover_color="#2563eb",
                command=lambda l=letra, c=q[6]:
                self.responder(l, c)
            )

            btn.pack(
                fill="x",
                padx=60,
                pady=10
            )

    # =====================================================
    # RESPONDER
    # =====================================================

    def responder(self, resposta, correta):

        if resposta == correta:
            self.pontos += 1

        self.index += 1

        if self.index >= len(self.perguntas):
            self.finalizar()
        else:
            self.mostrar_pergunta()

    # =====================================================
    # FINALIZAR
    # =====================================================

    def finalizar(self):

        nota = (
            self.pontos / len(self.perguntas)
        ) * 100

        self.db.salvar_resultado_quiz(
            self.usuario["id"],
            nota
        )

        for w in self.quiz_frame.winfo_children():
            w.destroy()

        resultado = ctk.CTkLabel(
            self.quiz_frame,
            text=f"🎉 Você acertou {self.pontos}/{len(self.perguntas)}\n\nNota: {nota:.0f}%",
            font=("Arial", 30, "bold"),
            text_color="#22c55e"
        )

        resultado.pack(expand=True)

        btn = ctk.CTkButton(
            self.quiz_frame,
            text="⬅ Voltar ao início",
            height=45,
            width=220,
            fg_color="#2563eb",
            hover_color="#1d4ed8",
            command=lambda: self.mudar_pagina("home")
        )

        btn.pack(pady=30)