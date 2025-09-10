
np = input("Digite o nome do produto: ")

vp = input("Digite o valor do produto: ")

qp = input("Digite a quantidade de produto: ")

print ("produto: ",np)
print ("valor: ",vp)
print("quantidade: ",qp)

with open("Produtos.txt", "a") as arquivo:
     arquivo.write (np + " | " + vp + " | " + qp +"\n")
