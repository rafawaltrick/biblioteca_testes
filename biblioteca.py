from gerenciar_livros import Livros
from gerenciar_usuarios import Usuarios

class Biblioteca:
    def __init__(self, livros: Livros, usuarios: Usuarios):
        self.livros = livros
        self.usuarios = usuarios

    def emprestar(self,titulo, nome_usuario):
        """Empresta um livro para um usuário."""
        if titulo in self.livros.livros:
            if nome_usuario in self.usuarios.usuarios:
                self.usuarios.usuarios[nome_usuario].append(titulo)
                return "Livro emprestado com sucesso!"
            else:
                return "Usuário não encontrado!"
        else:
            return "Livro não encontrado!"        
