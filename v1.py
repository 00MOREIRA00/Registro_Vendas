import psycopg2

conexao = psycopg2.connect(database = "estudando", host = "localhost", user = "postgres", password = "senha_fake", port = "5432")

idVenda = int(input("Digite o id de Venda: "))
cliente = input("Digite o nome do cliente: ")
produto = input("Digite o nome do produto: ")
data_venda = input("Digite a data da venda: ")
preco = int(input("Digite o preco do produto: "))
quantidade = (input("Digite a quantidade: "))

cur = conexao.cursor() 

cur.execute("INSERT INTO Vendas (id_venda, cliente, produto, data_venda, preco, quantidade) VALUES (%s, %s, %s, %s, %s, %s)", (idVenda, cliente, produto, data_venda, preco, quantidade))

conexao.commit()

# Close communication with the database
cur.close()
conexao.close()