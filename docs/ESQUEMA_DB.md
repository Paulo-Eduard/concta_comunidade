# Estrutura do Banco de Dados (SQLite)

- **usuarios:** ID, username, senha (hash), nome, email, telefone, tipo (aluno/professor), foto_path.
- **modulos:** ID, título e conteúdo do curso.
- **progresso:** Rastreia quais módulos o aluno concluiu.
- **quiz:** Armazena as perguntas, opções A, B, C, D e a resposta correta.
- **resultados:** Salva a nota final do aluno no quiz.
- **chat:** Armazena as mensagens com remetente_id e timestamp.