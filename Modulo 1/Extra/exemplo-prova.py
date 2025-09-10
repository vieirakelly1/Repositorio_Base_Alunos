
Usuarios = []

while True:
    print ("(1) Cadastrar pessoa.")
    print ("(2) Listar pessoas. ")
    print ("(3) Excluir pessoa. ")
    print ("(4) Sair.")
    opcao= input("Digite um numero: ")

    if opcao == '1':
        nome = input("Digite o usuário para cadastro: ")
        Usuarios.append (nome)
        print ("Usuário cadastrado.")

    elif opcao == '2':
       print ("Lista de pessoas pessoas cadastradas: ",Usuarios) 
        
    elif opcao == '3':
        print (Usuarios)
        nomedelete = input('Digite o nome que deseja remover: ')
        for item in Usuarios:
            if nomedelete == item:
                Usuarios.remove(input("Digite quem você deseja excluir: "))
                print("Usuário não encontrado")
                
            else:
                print(nomedelete, "removido com sucesso.")


    elif opcao == '4':
        print("Programa encerrado.")
        break
                                                                                                               