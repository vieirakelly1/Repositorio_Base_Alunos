#Validação de entrada: Peça ao usuário para digitar uma nota entre 0 e 10.
#Continue pedindo até que ele digite um valor válido.

nota= int(input('Digte uma nota entre 0 e 10: ') )

while nota <=0 or nota >10:
    nota = input("Digite a nota novamente")
print ("nota enviada.")