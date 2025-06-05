## Hamburgueria Delícia - Aplicação Web de Cardápio

Este projeto consiste em uma aplicação web para uma hamburgueria, apresentando o cardápio de forma interativa. O backend é construído com Flask (Python), fornecendo uma API para os dados do menu, enquanto o frontend (HTML, CSS, JavaScript) consome essa API para exibir o cardápio dinamicamente.

## Visão Geral

A aplicação possui as seguintes seções:

-   **Home:** Uma página inicial com uma chamada para ação para visualizar o cardápio.
-   **Cardápio:** Exibe os itens do menu (hambúrgueres, acompanhamentos e bebidas) carregados via API. Os usuários podem navegar entre as categorias.
-   **Sobre Nós:** Uma breve descrição da hamburgueria.
-   **Fale Conosco:** Um formulário de contato simples.

## Tecnologias Utilizadas

-   **Backend:**
    -   [Python](https://www.python.org/)
    -   [Flask](https://flask.palletsprojects.com/en/2.3.x/)
-   **Frontend:**
    -   HTML
    -   CSS (com [Tailwind CSS](https://tailwindcss.com/) para estilos utilitários e estilos customizados em `static/style.css`)
    -   JavaScript (`static/script.js`) para interatividade e comunicação com a API.

## Como Executar

1.  **Pré-requisitos:**
    -   Python 3 instalado.
    -   `pip` (gerenciador de pacotes do Python).

2.  **Instalação do Backend:**
    ```bash
    pip install Flask
    ```

3.  **Estrutura de Arquivos:**
    Certifique-se de ter a seguinte estrutura de arquivos:
    ```
    hamburgueria-delicia/
    ├── app.py
    ├── templates/
    │   └── index.html
    └── static/
        ├── style.css
        └── script.js
    └── README.md
    ```
    *(O script `app.py` cria os diretórios `templates` e `static` e seus respectivos arquivos na primeira execução, caso não existam.)*

4.  **Execução do Servidor Flask:**
    No terminal, navegue até o diretório raiz do projeto (`hamburgueria-delicia/`) e execute:
    ```bash
    python app.py
    ```
    O servidor de desenvolvimento do Flask estará rodando em `http://127.0.0.1:5000/`.

5.  **Acessando a Aplicação:**
    Abra seu navegador web e acesse o endereço fornecido pelo terminal (geralmente `http://127.0.0.1:5000/`).

## Endpoints da API

-   `/api/menu/hamburgueres`: Retorna um JSON com a lista de hambúrgueres.
-   `/api/menu/acompanhamentos`: Retorna um JSON com a lista de acompanhamentos.
-   `/api/menu/bebidas`: Retorna um JSON com a lista de bebidas.
-   `/api/menu/<categoria>`: Retorna um JSON com os itens da categoria especificada. Se a categoria não for encontrada, retorna um erro 404.

## Próximos Passos (Opcional)

-   Implementar funcionalidades de carrinho de compras.
-   Adicionar autenticação para um painel administrativo.
-   Melhorar o design e a responsividade.
-   Adicionar testes unitários e de integração para o backend.

## Contribuidores

-   Alysson Carlos Camelo Louzeiro      MAT. 202402242636
-   Arthur Silva Paixão de Oliveira     MAT. 202404151727
-   kAUÃ Antônio Rodriguês Moura        MAT. 202408700342
-   Pietro Giovani Oliveira da Silva    MAT. 202001285873
---