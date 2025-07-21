email = """
 Olá, %(nome)s
 Tem interesse em comprar %(produto)s? 
 Este produto é ótimo para %(texto)s!
 Clique agora em %(link)s
 Apenas %(quantidade)d disponíveis!
 Preço promocional de %(preco)f
 """
clientes = ["Maria", "João", "Bruno"]

for cliente in clientes:
    print(email % {"nome": cliente, "produto": "caneta","texto": "escrever muito bem",
      "link": "https://canetaslegais.com", "quantidade": 1, "preco": 49.99}


