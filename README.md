# Automação de Cadastro de Produtos com Python

Projeto de uma automação desenvolvida em Python para realizar o cadastro de produtos em um sistema web.

A automação utiliza a biblioteca **PyAutoGUI** para controlar o mouse e o teclado e **Pandas** para ler base de dados em formato CSV.

## Objetivo do projeto

Praticar conceitos de automação de tarefas utilizando Python, simulando o preenchimento repetitivo de formulários em sistemas web a partir de uma base de dados.

Este projeto foi desenvolvido para fins educacionais, como exercício de aprendizado em automação e manipulação de dados.

## Tecnologias utilizadas

- Python
- PyAutoGUI
- Pandas
- OpenPyXL

## Funcionalidades

A automação realiza as seguintes etapas:

1. Abre o navegador 
2. Acessa um sistema web
3. Realiza o login no sistema
4. Importa uma base de dados em CSV
5. Preenche automaticamente o formulário de cadastro de produtos
6. Repete o processo até finalizar todos os registros

## Estrutura do projeto

automacao-cadastro-produtos-python
│
├── automacao.py
├── produtos.csv
├── requirements.txt
├── README.md
└── .gitignore

## Como executar o projeto

1. Clone este repositório

git clone https://github.com/marinacarmona09/automacao-cadastro-produtos-python.git

2. Instale as dependências

pip install -r requirements.txt

3. Execute o script

python automacao.py

## Observações

- As coordenadas utilizadas pelo PyAutoGUI podem variar dependendo da resolução da tela e do ambiente de execução.
- O login presente no código é ilustrativo.