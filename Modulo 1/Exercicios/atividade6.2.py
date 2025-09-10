#Exercício 2: For + If/Else
#Enunciado: Escreva um programa que analise uma lista de números fornecida pelo usuário.
#Para cada número na lista, o programa deve determinar e exibir se ele é positivo, negativo ou zero. 
# Além disso, no final, deve contar e mostrar a quantidade de números positivos,negativos e zeros encontrados.
# Exemplo de Saída:
# text
# Digite os números separados por espaço: 5 -2 0 8 -1 0
# 5 é positivo.
# -2 é negativo.
# 0 é zero.
# 8 é positivo.
# -1 é negativo.
# 0 é zero.
# Relatório:
# Positivos: 2
# Negativos: 2
# Zeros: 2

lista=[2,34,5,567,-6,-7,5,0]
contPositivo=0
contNegativo=0
contZero=0
for item in lista:
    if item == 0:
        contZero=contZero + 1
       
    elif item <0:
        contNegativo=contNegativo + 1
       
    else:
        contPositivo= contPositivo + 1
        


print (contZero)
print(contNegativo)
print(contPositivo)
         
        
 