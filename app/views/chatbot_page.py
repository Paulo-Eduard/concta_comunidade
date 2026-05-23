import customtkinter as ctk
from tkinter import messagebox
import threading
from app.services.ia_service import IAService


class ChatbotPage(ctk.CTkFrame):

    def __init__(self, master, voltar_callback):
        super().__init__(master)

        self.voltar_callback = voltar_callback
        self.ia = IAService()

        self.configure(fg_color="#0f172a")

        # ================= HEADER =================
        header = ctk.CTkFrame(self, height=80, fg_color="#111827")
        header.pack(fill="x")
        header.pack_propagate(False)

        ctk.CTkButton(
            header,
            text="⬅ Voltar",
            fg_color="#2563eb",
            command=self.voltar
        ).pack(side="left", padx=20)

        ctk.CTkLabel(
            header,
            text="🤖 Assistente IA",
            font=("Arial", 26, "bold"),
            text_color="white"
        ).pack(side="left", padx=20)

        # ================= CHAT =================
        self.chat_box = ctk.CTkScrollableFrame(self)
        self.chat_box.pack(fill="both", expand=True, padx=20, pady=20)

        # ================= INPUT =================
        bottom = ctk.CTkFrame(self, fg_color="transparent")
        bottom.pack(fill="x", padx=20, pady=10)

        self.entry = ctk.CTkEntry(bottom, placeholder_text="Digite sua pergunta...")
        self.entry.pack(side="left", fill="x", expand=True, padx=(0, 10))

        self.btn = ctk.CTkButton(
            bottom,
            text="Enviar",
            command=self.enviar
        )
        self.btn.pack(side="right")

    # ================= VOLTAR =================
    def voltar(self):
        self.voltar_callback("home")

    # ================= ENVIAR =================
    def enviar(self):

        pergunta = self.entry.get().strip()

        if not pergunta:
            return

        self.add_msg("Você", pergunta)
        self.entry.delete(0, "end")

        # trava UI? NÃO MAIS 👇
        threading.Thread(
            target=self.processar_ia,
            args=(pergunta,),
            daemon=True
        ).start()

    # ================= IA THREAD =================
    def processar_ia(self, pergunta):

        resposta = self.ia.responder(pergunta)

        self.add_msg("IA", resposta)

    # ================= UI MSG =================
    def add_msg(self, autor, texto):

        frame = ctk.CTkFrame(self.chat_box, fg_color="#1e293b")
        frame.pack(fill="x", pady=5)

        ctk.CTkLabel(
            frame,
            text=f"{autor}:",
            text_color="#60a5fa",
            font=("Arial", 14, "bold")
        ).pack(anchor="w", padx=10, pady=(5, 0))

        ctk.CTkLabel(
            frame,
            text=texto,
            wraplength=800,
            justify="left"
        ).pack(anchor="w", padx=10, pady=(0, 10))