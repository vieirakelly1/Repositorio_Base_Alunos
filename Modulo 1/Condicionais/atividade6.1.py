#Exercício 1: If/Else (Múltiplas Condições)Enunciado: Escreva um programa que determine o preço do ingresso de cinema 
# baseado na idade do cliente e se é estudante. As regras são: Crianças até 12 anos: R$ 8,00mEstudantes (com carteirinha)
#  de qualquer idade: R$ 12,00 Idosos (65+ anos): R$ 10,00 Adultos (13-64 anos) não estudantes: R$ 20,00 
# O programa deve perguntar idade e se é estudante.

# Exemplo de Saída:
# text
# Digite sua idade: 18
# É estudante? (s/n): s
# Preço do ingresso: R$ 12.00


idade = int(input("digite sua idade: "))
estudante = input('É estudante?(s/n): ')

if idade <=12:
    print ('R$', 8.00)

if estudante == 's':
    print ('R$', 12.00)
    
elif idade >=65:
    print ('R$', 10.00)
else:
    print ('R$', 20.00)


