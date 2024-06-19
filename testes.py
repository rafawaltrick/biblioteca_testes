import unittest
from gerenciar_livros import Livros
from gerenciar_usuarios import Usuarios
from biblioteca import Biblioteca

class TestBiblioteca(unittest.TestCase):

    def setUp(self):
        self.livros = Livros()
        self.usuarios = Usuarios()
        self.biblioteca = Biblioteca(self.livros, self.usuarios)

    def test_bottom_up(self):
        # Teste adicionar livro
        resultado_adicionar_livro = self.livros.adicionar_livro("O Hobbit", "J.R.R. Tolkien")
        self.assertEqual(resultado_adicionar_livro, "Livro adicionado com sucesso!")
        self.assertIn("O Hobbit", self.livros.livros)

        # Teste adicionar usuário
        resultado_adicionar_usuario = self.usuarios.adicionar_usuario("Bilbo Bolseiro")
        self.assertEqual(resultado_adicionar_usuario, "Usuário adicionado com sucesso!")
        self.assertIn("Bilbo Bolseiro", self.usuarios.usuarios)

        # Teste emprestar livro
        resultado_emprestar = self.biblioteca.emprestar("O Hobbit", "Bilbo Bolseiro")
        self.assertEqual(resultado_emprestar, "Livro emprestado com sucesso!")
        self.assertIn("O Hobbit", self.usuarios.usuarios["Bilbo Bolseiro"])

    def test_top_down(self):
        # Simula a adição de livro e usuário
        self.livros.livros = {"O Hobbit": "J.R.R. Tolkien"}
        self.usuarios.usuarios = {"Bilbo Bolseiro": []}

        # Testa o empréstimo
        resultado_emprestar = self.biblioteca.emprestar("O Hobbit", "Bilbo Bolseiro")
        self.assertEqual(resultado_emprestar, "Livro emprestado com sucesso!")
        self.assertIn("O Hobbit", self.usuarios.usuarios["Bilbo Bolseiro"])

    def test_big_bang(self):
        # Adiciona livro e usuário
        resultado_adicionar_livro = self.livros.adicionar_livro("O Hobbit", "J.R.R. Tolkien")
        self.assertEqual(resultado_adicionar_livro, "Livro adicionado com sucesso!")
        resultado_adicionar_usuario = self.usuarios.adicionar_usuario("Bilbo Bolseiro")
        self.assertEqual(resultado_adicionar_usuario, "Usuário adicionado com sucesso!")

        # Testa o empréstimo
        resultado_emprestar = self.biblioteca.emprestar("O Hobbit", "Bilbo Bolseiro")
        self.assertEqual(resultado_emprestar, "Livro emprestado com sucesso!")
        self.assertIn("O Hobbit", self.usuarios.usuarios["Bilbo Bolseiro"])

if __name__ == '__main__':
    unittest.main()
