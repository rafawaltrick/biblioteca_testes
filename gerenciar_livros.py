class Livros:
    def __init__(self):
        self.livros = {}

    def adicionar_livro(self, titulo, autor):
        """Adiciona um livro ao sistema."""
        if titulo not in self.livros:  # Verifica se o livro NÃO existe
            self.livros[titulo] = autor
            return "Livro adicionado com sucesso!"
        else:
            return "Livro já cadastrado!"

    def remover_livro(self, titulo):
        """Remove um livro do sistema."""
        if titulo in self.livros:
            del self.livros[titulo]
            return "Livro removido com sucesso!"
        else:
            return "Livro não encontrado!"

    def listar_livros(self):
        """Lista todos os livros cadastrados."""
        if self.livros:
            return self.livros
        
   
