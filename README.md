# Teste de Integração de Biblioteca - Exemplo em Python

Este projeto demonstra a aplicação de diferentes técnicas de teste de integração (bottom-up, top-down e big-bang) em um sistema de biblioteca simplificado em Python.

## Estrutura do Projeto

*   **`gerenciar_livros.py`:** Contém funções para adicionar, remover e listar livros.
*   **`gerenciar_usuarios.py`:** Contém funções para adicionar, remover e listar usuários.
*   **`biblioteca.py`:** Contém a classe `Biblioteca` que gerencia o empréstimo de livros.
*   **`testes.py`:** Contém os testes unitários e de integração utilizando o framework `unittest`.

## Como Executar os Testes

1.  **Pré-requisitos:**
    *   Certifique-se de ter o Python instalado em seu sistema.
    *   Instale o `unittest` (normalmente já incluso na instalação padrão do Python).

2.  **Clone o Repositório:**
    ```bash
    git clone https://github.com/rafawaltrick/biblioteca_testes/tree/main
    ```

3.  **Acesse o Diretório do Projeto:**
    ```bash
    cd biblioteca_testes
    ```

4.  **Execute os Testes:**
    ```bash
    python3 testes.py
    ```

## Abordagens de Teste

*   **Bottom-up:** Testa cada módulo individualmente e depois a integração entre eles.
*   **Top-down:** Testa o módulo principal simulando a interação com os outros módulos.
*   **Big-bang:** Testa todo o sistema de uma vez após a implementação completa.

## Observações

*   Este projeto é um exemplo simplificado para fins didáticos. Em um sistema real, os testes seriam mais complexos e abrangentes.
