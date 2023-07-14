import psycopg2

conexao = psycopg2.connect(database = "estudando", host = "localhost", user = "postgres", password = "senha_fake", port = "5432")

#print(conexao.info)
#print(conexao.status)

cur = conexao.cursor() 

cur.execute("INSERT INTO Vendas (id_venda, cliente, produto, data_venda, preco, quantidade) VALUES (%s, %s, %s, %s, %s, %s)", (3,"Jack","Iphone", "16/10/2023", 7000, 1))

conexao.commit()

# Close communication with the database
cur.close()
conexao.close()