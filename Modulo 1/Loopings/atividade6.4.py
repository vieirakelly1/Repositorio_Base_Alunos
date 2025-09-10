# : While + If/Else (com acumulador)
# Enunciado: Crie um programa de controle de estoque simples. O programa deve começar
# com 50 unidades de um produto. O usuário pode:
# (1) Adicionar unidades ao estoque
# (2) Remover unidades do estoque
# (3) Verificar estoque atual
# (4) Sair
# Não permita que o estoque fique negativo.

estoque = 50
while True:
    print ("(1) Adicionar unidades ao estoque")
    print ("(2) Remover unidades do estoque")
    print ("(3) Verificar estoque atual")
    print ("(4) Sair")
    opcao=input("Digite um numero: ")

    if opcao == "1":
       adicionar = int(input("Unidade(s) para adicionar: "))
       estoque= estoque+ adicionar
       print(estoque)

    if opcao == "2":
       remover = int(input("Unidade(s) para remover: "))
       estoque= estoque- remover
       print (estoque)

    if opcao == "3":
       print (estoque)

    if opcao=="4":
       break
       



