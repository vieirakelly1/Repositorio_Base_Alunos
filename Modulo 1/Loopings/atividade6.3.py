# Exercício 3: While + If/Else
# Enunciado: Crie um programa que simule um caixa eletrônico simples. O programa deve
# iniciar com um saldo de R$ 1000,00. Ele deve apresentar um menu com as opções: (1)
# Sacar, (2) Depositar, (3) Ver Saldo e (4) Sair. O loop deve continuar até que o usuário
# escolha a opção 4. Para saques, não deve ser permitido sacar mais do que o saldo
# disponível.
# Exemplo de Saída:
# text
# Caixa Eletrônico
# (1) Sacar
# (2) Depositar
# (3) Ver Saldo
# (4) Sair
# Opção: 1
# Valor para sacar: 500
# Saque realizado com sucesso!
# ...
# Opção: 4
# Obrigado por usar nossos serviços!

numero = 1000
while True:
    
    opcao=input('digite um numero')
    print ("(1) Sacar")
    print ("(2) Depositar")
    print ("(3) Ver Saldo")
    print ("(4) Sair")
    if opcao=="1":
        saque=int(input("valor para sacar: "))
        numero=numero- saque
        print('Saque realizado com sucesso!')
        
    if opcao=="3":
        print (numero)

    if opcao=='4':
        print("Obrigado por usar nossos serviços!")
        break

