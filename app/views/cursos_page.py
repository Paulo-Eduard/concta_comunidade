import customtkinter as ctk
from tkinter import messagebox


class CursosPage(ctk.CTkFrame):

    def __init__(self, master, mudar_pagina_callback, usuario_logado, db):
        super().__init__(master)

        self.db = db
        self.usuario = usuario_logado
        self.mudar_pagina = mudar_pagina_callback

        # =========================================
        # CONFIGURAÇÃO GERAL
        # =========================================

        self.configure(fg_color="#0f172a")

        # =========================================
        # HEADER
        # =========================================

        self.header = ctk.CTkFrame(
            self,
            height=80,
            fg_color="#111827",
            corner_radius=0
        )

        self.header.pack(fill="x")
        self.header.pack_propagate(False)

        self.btn_voltar = ctk.CTkButton(
            self.header,
            text="⬅ Voltar",
            width=120,
            height=40,
            fg_color="#2563eb",
            hover_color="#1d4ed8",
            font=("Arial", 14, "bold"),
            command=lambda: self.mudar_pagina("home")
        )

        self.btn_voltar.pack(side="left", padx=20)

        titulo = ctk.CTkLabel(
            self.header,
            text="📚 Central de Cursos",
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

        # =========================================
        # CONTAINER PRINCIPAL
        # =========================================

        self.main = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.main.pack(fill="both", expand=True, padx=20, pady=20)

        # =========================================
        # SIDEBAR
        # =========================================

        self.sidebar = ctk.CTkFrame(
            self.main,
            width=250,
            fg_color="#111827",
            corner_radius=15
        )

        self.sidebar.pack(side="left", fill="y", padx=(0, 20))
        self.sidebar.pack_propagate(False)

        menu_titulo = ctk.CTkLabel(
            self.sidebar,
            text="📘 Menu",
            font=("Arial", 22, "bold")
        )

        menu_titulo.pack(pady=25)

        menus = [

            ("🏠 Início", "home"),

            ("📚 Cursos", "cursos"),

            ("🧠 Quiz", "quiz"),

            ("🤖 IA", "chatbot"),

            ("👤 Perfil", "perfil")
        ]

        for texto, destino in menus:

            btn = ctk.CTkButton(

                self.sidebar,

                text=texto,

                height=45,

                fg_color="#1e293b",

                hover_color="#2563eb",

                anchor="w",

                font=("Arial", 14),

                command=lambda d=destino:
                self.mudar_pagina(d)
            )

            btn.pack(
                fill="x",
                padx=15,
                pady=8
            )

        # =========================================
        # CONTEÚDO
        # =========================================

        self.content = ctk.CTkFrame(
            self.main,
            fg_color="transparent"
        )

        self.content.pack(side="right", fill="both", expand=True)

        # =========================================
        # PROFESSOR / ALUNO
        # =========================================

        if self.usuario.get("tipo") == "professor":
            self.criar_painel_professor()

        else:
            self.criar_painel_aluno()

    # =====================================================
    # PAINEL PROFESSOR
    # =====================================================

    def criar_painel_professor(self):

        top = ctk.CTkFrame(
            self.content,
            fg_color="#111827",
            corner_radius=20
        )

        top.pack(fill="x", pady=(0, 20))

        titulo = ctk.CTkLabel(
            top,
            text="➕ Criar Novo Curso",
            font=("Arial", 24, "bold")
        )

        titulo.pack(pady=(20, 10))

        self.entry_titulo = ctk.CTkEntry(
            top,
            placeholder_text="Título do módulo...",
            height=45,
            font=("Arial", 15),
            corner_radius=12
        )

        self.entry_titulo.pack(fill="x", padx=20, pady=10)

        self.textbox_conteudo = ctk.CTkTextbox(
            top,
            height=180,
            corner_radius=12,
            font=("Arial", 14)
        )

        self.textbox_conteudo.pack(fill="x", padx=20, pady=10)

        btn_add = ctk.CTkButton(
            top,
            text="🚀 Publicar Curso",
            height=45,
            font=("Arial", 15, "bold"),
            fg_color="#2563eb",
            hover_color="#1d4ed8",
            corner_radius=12,
            command=self.salvar_modulo
        )

        btn_add.pack(pady=20)

        lista_titulo = ctk.CTkLabel(
            self.content,
            text="📚 Cursos Publicados",
            font=("Arial", 24, "bold")
        )

        lista_titulo.pack(anchor="w", pady=10)

        self.frame_modulos = ctk.CTkScrollableFrame(
            self.content,
            fg_color="#111827",
            corner_radius=20
        )

        self.frame_modulos.pack(fill="both", expand=True)

        self.lista_modulos_prof()

    # =====================================================
    # LISTAR CURSOS
    # =====================================================

    def lista_modulos_prof(self):

        for widget in self.frame_modulos.winfo_children():
            widget.destroy()

        modulos = self.db.obter_modulos()

        if not modulos:

            vazio = ctk.CTkLabel(
                self.frame_modulos,
                text="Nenhum curso publicado ainda.",
                font=("Arial", 16)
            )

            vazio.pack(pady=30)

            return

        for modulo in modulos:

            card = ctk.CTkFrame(
                self.frame_modulos,
                fg_color="#1e293b",
                corner_radius=18
            )

            card.pack(fill="x", padx=15, pady=10)

            titulo = ctk.CTkLabel(
                card,
                text=f"📘 {modulo[1]}",
                font=("Arial", 20, "bold")
            )

            titulo.pack(anchor="w", padx=20, pady=(15, 5))

            descricao = ctk.CTkLabel(
                card,
                text=modulo[2][:150] + "...",
                justify="left",
                wraplength=700,
                text_color="#cbd5e1",
                font=("Arial", 14)
            )

            descricao.pack(anchor="w", padx=20, pady=(0, 15))

            botoes = ctk.CTkFrame(
                card,
                fg_color="transparent"
            )

            botoes.pack(
                fill="x",
                padx=20,
                pady=(0, 15)
            )

            btn_abrir = ctk.CTkButton(
                botoes,
                text="👁 Abrir",
                width=120,
                fg_color="#2563eb",
                hover_color="#1d4ed8",
                command=lambda c=modulo[2]:
                self.visualizar_modulo(c)
            )

            btn_abrir.pack(side="left")

            btn_excluir = ctk.CTkButton(
                botoes,
                text="🗑 Excluir",
                width=120,
                fg_color="#dc2626",
                hover_color="#b91c1c",
                command=lambda id=modulo[0]:
                self.deletar_modulo(id)
            )

            btn_excluir.pack(side="right")

    # =====================================================
    # VISUALIZAR CURSO
    # =====================================================

    def visualizar_modulo(self, conteudo):

        janela = ctk.CTkToplevel(self)

        janela.title("Visualizar Curso")
        janela.geometry("900x600")

        janela.grab_set()
        janela.focus()

        frame = ctk.CTkFrame(
            janela,
            fg_color="#0f172a"
        )

        frame.pack(fill="both", expand=True)

        texto = ctk.CTkTextbox(
            frame,
            font=("Arial", 15)
        )

        texto.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        texto.insert("1.0", conteudo)

    # =====================================================
    # SALVAR CURSO
    # =====================================================

    def salvar_modulo(self):

        titulo = self.entry_titulo.get().strip()

        conteudo = self.textbox_conteudo.get(
            "1.0",
            "end-1c"
        ).strip()

        if not titulo or not conteudo:

            messagebox.showwarning(
                "Campos vazios",
                "Preencha todos os campos."
            )

            return

        self.db.adicionar_modulo(
            titulo,
            conteudo
        )

        messagebox.showinfo(
            "Sucesso",
            "Curso publicado!"
        )

        self.entry_titulo.delete(0, "end")

        self.textbox_conteudo.delete(
            "1.0",
            "end"
        )

        self.lista_modulos_prof()

    # =====================================================
    # EXCLUIR
    # =====================================================

    def deletar_modulo(self, modulo_id):

        confirmar = messagebox.askyesno(
            "Excluir",
            "Deseja excluir este curso?"
        )

        if confirmar:

            self.db.excluir_modulo(modulo_id)

            messagebox.showinfo(
                "Sucesso",
                "Curso removido!"
            )

            self.lista_modulos_prof()

    # =====================================================
    # PAINEL ALUNO
    # =====================================================

    def criar_painel_aluno(self):

        modulos = self.db.obter_modulos()

        concluidos = self.db.obter_progresso(
            self.usuario["id"]
        )

        total = len(modulos)

        progresso = (
            len(concluidos) / total
            if total > 0 else 0
        )

        progresso_card = ctk.CTkFrame(
            self.content,
            fg_color="#111827",
            corner_radius=20
        )

        progresso_card.pack(
            fill="x",
            pady=(0, 20)
        )

        titulo = ctk.CTkLabel(
            progresso_card,
            text="📈 Seu Progresso",
            font=("Arial", 24, "bold")
        )

        titulo.pack(pady=(20, 10))

        barra = ctk.CTkProgressBar(
            progresso_card,
            width=600,
            height=18,
            progress_color="#2563eb"
        )

        barra.pack(pady=10)

        barra.set(progresso)

        porcentagem = int(progresso * 100)

        texto = ctk.CTkLabel(
            progresso_card,
            text=f"{porcentagem}% concluído",
            font=("Arial", 16)
        )

        texto.pack(pady=(0, 20))

        self.scroll = ctk.CTkScrollableFrame(
            self.content,
            fg_color="transparent"
        )

        self.scroll.pack(
            fill="both",
            expand=True
        )

        for modulo in modulos:

            concluido = modulo[0] in concluidos

            card = ctk.CTkFrame(
                self.scroll,
                fg_color="#111827",
                corner_radius=20
            )

            card.pack(fill="x", pady=12)

            status = "✅" if concluido else "📘"

            titulo = ctk.CTkLabel(
                card,
                text=f"{status} {modulo[1]}",
                font=("Arial", 22, "bold")
            )

            titulo.pack(
                anchor="w",
                padx=20,
                pady=(20, 5)
            )

            resumo = modulo[2][:180] + "..."

            descricao = ctk.CTkLabel(
                card,
                text=resumo,
                justify="left",
                wraplength=750,
                text_color="#cbd5e1",
                font=("Arial", 14)
            )

            descricao.pack(anchor="w", padx=20)

            btn = ctk.CTkButton(
                card,
                text="🚀 Abrir Curso",
                width=180,
                height=42,
                fg_color="#2563eb",
                hover_color="#1d4ed8",
                font=("Arial", 14, "bold"),
                command=lambda m_id=modulo[0], c=modulo[2]:
                self.abrir_e_concluir(m_id, c)
            )

            btn.pack(
                anchor="e",
                padx=20,
                pady=20
            )

    # =====================================================
    # ABRIR CURSO
    # =====================================================

    def abrir_e_concluir(self, modulo_id, conteudo):

        janela = ctk.CTkToplevel(self)

        janela.title("Conteúdo do Curso")
        janela.geometry("900x600")

        janela.grab_set()
        janela.focus()

        frame = ctk.CTkFrame(
            janela,
            fg_color="#0f172a"
        )

        frame.pack(fill="both", expand=True)

        texto = ctk.CTkTextbox(
            frame,
            font=("Arial", 15)
        )

        texto.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        texto.insert("1.0", conteudo)

        btn = ctk.CTkButton(
            frame,
            text="✅ Marcar como concluído",
            height=45,
            fg_color="#16a34a",
            hover_color="#15803d",
            command=lambda:
            self.concluir_modulo(
                janela,
                modulo_id
            )
        )

        btn.pack(pady=20)

    # =====================================================
    # CONCLUIR
    # =====================================================

    def concluir_modulo(self, janela, modulo_id):

        self.db.marcar_modulo_concluido(
            self.usuario["id"],
            modulo_id
        )

        janela.destroy()

        messagebox.showinfo(
            "Parabéns!",
            "Curso concluído!"
        )

        self.content.destroy()

        self.content = ctk.CTkFrame(
            self.main,
            fg_color="transparent"
        )

        self.content.pack(
            side="right",
            fill="both",
            expand=True
        )

        self.criar_painel_aluno()

    # =====================================================
    # CERTIFICADO
    # =====================================================

    def emitir_certificado(self):

        messagebox.showinfo(
            "Certificado",
            f"🏆 Certificado emitido para {self.usuario['nome']}!"
        )