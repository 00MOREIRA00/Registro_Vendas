# Registro_Vendas
Esse diretório tem como objetivo estudar a conexão de banco de dados usando Python: O objetivo desse desenvolvimento é criar um Script onde prenchemos as informações solicitadas e ela preencha no Banco de Dados criado.

## Recursos

* Postgresql
* Biblioteca psycopg2

## Como foi feito? 

Inicialmente criamos um Data Base
```
CREATE DATABASE estudando
```

Criamos uma tabela para receber as informações
```
CREATE TABLE Vendas(
	id_venda int,
	cliente varchar(50),
	produto varchar(50),
	data_venda date,
	preco decimal(6, 2),
	quantidade int
)
```




