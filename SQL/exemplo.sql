create DATABASE exemplo_db;
USE exemplo_db; --banco de dados chamado exemplo_db, use só pode ser usado com o banco de dados
create table usuarios ( --tabela chamada usuarios
    usuario char(50) not null,--nesse exemplo a tabela usuarios tem duas colunas: usuario e senha
    senha char(50) not null
);
insert into usuarios (usuario, senha) values ('admin', 'senhafoda123');
insert into usuarios (usuario, senha) values ('user', 'user123');
insert into usuarios (usuario, senha) values ('fulano', 'fulano123');
select * from usuarios;--mostra todos os dados da tabela usuarios
create user "admin"@"localhost" identified by "senhafoda123";
grant all privileges on exemplo_db.* to "admin"@"localhost"; --esse comando dá todos os privilégios do banco de dados exemplo_db para o usuário admin
flush privileges;
exit;

--describe só pode ser usado com tabelas e serve para mostrar a estrutura da tabela
--use só pode ser usado com banco de dados e serve para selecionar o banco de dados que
