## Sobre 

Este projeto foi desenvolvido como parte da avaliação do módulo Ciência da Computaçãocurso do curso Desenvolvimento Web da escola Trybe e foi desenvolvido em Python.

Nele foi desenvolvido um programa que tem como principal objetivo fazer consultas em notícias sobre tecnologia, através da técnica de raspagem de dados. Aqui foi utilizado o blog da Trybe(https://blog.betrybe.com).

### Habilidades a serem trabalhadas:

- Utilizar o terminal interativo do Python;
- Escrever seus próprios módulos e importá-los em outros códigos;
- Aplicar técnicas de raspagem de dados;
- Extrair dados de conteúdo HTML;
- Armazenar os dados obtidos em um banco de dados.

### Para executar o projeto localmente:

- Clone o repositório
```
  git clone git@github.com:Ivan-Mastrangelo/tech-news.git
```
- Entre na pasta do repositório que você acabou de clonar:
```
  cd tech-news
  ```
- Crie o ambiente virtual para o projeto
```
  python3 -m venv .venv && source .venv/bin/activate
 ```
- Instale as dependências
```
  python3 -m pip install -r dev-requirements.txt
  ```
#### Teste Manual
  
  Abra um terminal Python importando as funções de interesse através do comando:
  ```
  python3 -i tech_news/arquivo_de_interesse.py
  ```
  Neste projeto, foi utilizado um banco de dados chamado `tech_news`.
  As notícias serão armazenadas em uma coleção chamada `news`.
  A Trybe disponibilizou algumas funções prontas no arquivo `tech_news/database.py` para minipulação do Banco de Dados em Mongodb.

  Para rodar MongoDB via Docker:
  ```
    docker-compose up -d mongodb</code> no terminal. 
  ```

  Caso queira instalar e rodar o servidor MongoDB nativo na máquina, sem o uso do docker, siga as instruções no tutorial oficial:

  Ubuntu: https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/
  MacOS:  https://docs.mongodb.com/guides/server/install/
  
  Com o banco de dados rodando, o nosso módulo conseguirá acessá-lo sem problemas. Importe o módulo `tech_news/database.py` e chame as funções contidas nele.
  Lembre-se de que o mongoDB utilizará por padrão a porta 27017. Se já houver outro serviço utilizando esta porta, considere desativá-lo.
  
