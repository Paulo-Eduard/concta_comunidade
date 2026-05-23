import ollama


class IAService:

    def responder(self, pergunta: str) -> str:
        try:
            resposta = ollama.chat(
                model="phi3",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "Você é um assistente virtual de alfabetização digital "
                            "e segurança online. Responda de forma simples e clara."
                        )
                    },
                    {
                        "role": "user",
                        "content": pergunta
                    }
                ]
            )

            return resposta["message"]["content"]

        except Exception as e:
            return f"Erro na IA: {str(e)}"