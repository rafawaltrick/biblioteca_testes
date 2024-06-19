class Usuarios:
    def __init__(self):
        self.usuarios = {}

    def adicionar_usuario(self, nome):
        """Adiciona um usuário ao sistema."""
        if nome not in self.usuarios:  # Verifica se o usuário NÃO existe
            self.usuarios[nome] = []
            return "Usuário adicionado com sucesso!"
        else:
            return "Usuário já cadastrado!"

    def remover_usuario(self, nome):
        """Remove um usuário do sistema."""
        if nome in self.usuarios:
            del self.usuarios[nome]
            return "Usuário removido com sucesso!"
        else:
            return "Usuário não encontrado!"

    def listar_usuarios(self):
        """Lista todos os usuários cadastrados."""
        if self.usuarios:
            return self.usuarios
