import customtkinter as ctk

class ChatPage(ctk.CTkFrame):
    def __init__(self, master, voltar_callback, usuario_logado, db):
        super().__init__(master, fg_color="transparent")
        self.db = db
        self.usuario = usuario_logado
        
        ctk.CTkButton(self, text="⬅ Voltar", command=voltar_callback).pack(anchor="nw", padx=20, pady=20)
        
        # Área de visualização das mensagens
        self.chat_area = ctk.CTkScrollableFrame(self, width=500, height=300)
        self.chat_area.pack(pady=10)
        
        # Campo de entrada
        self.input_msg = ctk.CTkEntry(self, placeholder_text="Digite sua mensagem...", width=400)
        self.input_msg.pack(pady=10)
        ctk.CTkButton(self, text="Enviar", command=self.enviar).pack()
        
        self.carregar_mensagens()

    def carregar_mensagens(self):
        for w in self.chat_area.winfo_children(): w.destroy()
        for nome, msg in self.db.obter_mensagens():
            ctk.CTkLabel(self.chat_area, text=f"{nome}: {msg}", anchor="w").pack(fill="x", pady=2)

    def enviar(self):
        msg = self.input_msg.get()
        if msg:
            self.db.enviar_mensagem(self.usuario['id'], msg)
            self.input_msg.delete(0, 'end')
            self.carregar_mensagens()