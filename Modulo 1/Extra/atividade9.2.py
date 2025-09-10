from Atividades8.funcoes3 import dividir
a = int(input("Digite um número: "))
b = int(input("Digite um número: "))

try:
   dividir (a,b)
   print("A divisão entre a e b é: ",dividir)
except:
    print('None')