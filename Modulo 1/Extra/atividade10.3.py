# Crie um sistema que regista o nome e 3 notas do aluno depois você vai validar se a média
# do aluno é maior que 7 caso seja maior você deve registrar em um documento o nome dele
# e se ele está aprovado ou reprovado.O sistema deve estar em um loop e deve ser
# encerrado somente se o usuário digitar a opção 0


nome = input("Digite o nome do aluno: ")
nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))

while True:
    soma = (nota1 + nota2 + nota3)/3
    str(soma)

    if soma < 7:
     print ("Reprovado(a).")
     with open("Notas.txt", "a") as notas:
       notas.write (nome + " | " + str(soma) + " Reprovado(a)" + "\n")

    elif soma >= 7:
     print ("Aprovado(a).")
     with open("Notas.txt", "a") as notas:
       notas.write (nome + " | " + str(soma) + " Aprovado(a)" + "\n")
    
    numero = int(input("Digite zero para encerrar: "))
    if numero == 0:
       print("Programa encerrado.")
       break
     
    
       

    

