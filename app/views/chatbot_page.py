import customtkinter as ctk

from app.services.ia_service import IAService


class ChatbotPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.ia = IAService()

        titulo = ctk.CTkLabel(
            self,
            text="🤖 Assistente Virtual",
            font=("Arial", 30, "bold")
        )

        titulo.pack(pady=20)

        self.chat = ctk.CTkTextbox(
            self,
            width=850,
            height=450
        )

        self.chat.pack(pady=20)

        self.entrada = ctk.CTkEntry(
            self,
            width=600,
            placeholder_text="Digite sua pergunta"
        )

        self.entrada.pack(pady=10)

        botao = ctk.CTkButton(
            self,
            text="Enviar",
            command=self.enviar
        )

        botao.pack(pady=10)

    def enviar(self):

        pergunta = self.entrada.get()

        if pergunta.strip() == "":
            return

        resposta = self.ia.responder(
            pergunta
        )

        self.chat.insert(
            "end",
            f"Você: {pergunta}\n\n"
        )

        self.chat.insert(
            "end",
            f"IA: {resposta}\n\n"
        )

        self.entrada.delete(0, "end")