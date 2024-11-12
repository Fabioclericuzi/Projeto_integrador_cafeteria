## Projeto integrador(Cafeteria - Coffeebreack)

### Visão Geral 
Projeto realizado na linguagem Python que cria um sistema de uma cafeteria online para a realização de cadastros de usuários, contato com a cafeteria e a realização de pedidos online.
Sistema foi criado através da utilização do framework Django que permite a criação de interface gráfica e facilita as configurações necessárias para o deploy da aplicação de maneira
simples e eficaz. 

### 2. Arquitetura
2.1 Backend: Contém a aplicação python, um arquivo de serviços onde estão hospedadas as funções chamadas pela aplicação, um arquivo de teste e os arquivos docker(dockerfile e docker-compose)

2.2 Banco de dados: Se trata de um banco Mysql que armazena as informações dos pedidos, cadastro de usuário, contato com dos usuários com a cafeteria e dos produtos em estoque e suas quantidades.

2.3 Containers docker: A aplicação está hospedada em containers(o banco e a aplicação) que são executadas através de um arquivo docker-compose.
