## Projeto integrador(Cafeteria - Coffeebreack)

### Visão Geral 
Projeto realizado na linguagem Python que cria um sistema de uma cafeteria online para a realização de cadastros de usuários, contato com a cafeteria e a realização de pedidos online.
Sistema foi criado através da utilização do framework Django que permite a criação de interface gráfica e facilita as configurações necessárias para o deploy da aplicação de maneira
simples e eficaz. 

### 2. Arquitetura
2.1 Backend: Contém a aplicação python, um arquivo de serviços onde estão hospedadas as funções chamadas pela aplicação, um arquivo de teste e os arquivos docker(dockerfile e docker-compose)

2.2 Banco de dados: Se trata de um banco Mysql que armazena as informações dos pedidos, cadastro de usuário, contato com dos usuários com a cafeteria e dos produtos em estoque e suas quantidades.

2.3 Containers docker: A aplicação está hospedada em containers(o banco e a aplicação) que são executadas através de um arquivo docker-compose.

### 3. Como excutar o projeto
Para executar o projeto basta acessar a pasta do projeto(coffeebreak) e executar o comando 'docker-compose up --build'. Lembrando que se o projeto for executado no windows, é necessário que o docker desktop esteja rodando.

Após executar essas instruções, o projeto pode ser acessado no endereço http://localhost:8000. Todas as telas estarão disponíveis no endereço anteriormente enviado e os testes podem ser realizados nessa interface.
As informações serão armazenadas no banco de dados Mysql no databse chamado 'cafeteria'. Nesse database estarão disponíveis as tabelas de contato, estoque, item do pedido, pedido e usuários(também estarão presentes
as tabelas criadas automaticamente pelo Django).

Para a realização dos testes relacionados às views do Python, basta acessar o diretório de testes(app/tests) e executar o comando 'pytest test_views.py'. Para a realização dos testes dos códigos Javascript,
basta acessar o diretório raiz(coffeebreak) e executar o comando 'npm test'.

## 4. Considerações finais
Essa documentação fornece uma visão geral de configuração e execução da API utilizando docker compose para orquestrar os serviços do backend e do banco de dados.
