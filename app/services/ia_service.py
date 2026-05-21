import ollama


class IAService:

    def responder(self, pergunta):

        resposta = ollama.chat(

            model="phi3",

            messages=[

                {
                    "role": "system",
                    "content": (
                        "Você é um assistente virtual "
                        "de alfabetização digital e "
                        "segurança online."
                    )
                },

                {
                    "role": "user",
                    "content": pergunta
                }
            ]
        )

        return resposta["message"]["content"]