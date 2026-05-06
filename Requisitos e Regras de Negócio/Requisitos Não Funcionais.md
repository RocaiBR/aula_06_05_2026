# Requisitos Não Funcionais (RNF)

- RNF01 (Arquitetura): O sistema deve ser desenvolvido obrigatoriamente seguindo o padrão estrutural MVC em camadas
(View, Controller, Service, Repository), garantindo a separação de responsabilidades.

- RNF02 (Persistência e Integridade): O banco de dados utilizado será o SQLite,
e as operações de escrita devem utilizar o controle de transações (Commit/Rollback) para garantir a propriedade ACID dos dados.

- RNF03 (Confiabilidade/Tratamento de Erros): O sistema não deve falhar ou fechar abruptamente diante de erros de banco de dados ou entradas inválidas. Exceções devem ser capturadas e transformadas em mensagens amigáveis para o usuário.

- RNF04 (Usabilidade): As validações de regras de negócio (como formatos de horas e capacidades) 
devem ocorrer antes da tentativa de persistência no banco, otimizando o tempo de resposta do sistema.
