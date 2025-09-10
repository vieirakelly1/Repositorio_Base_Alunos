# Lista Inicial
nomes = ["Joaquim","Maria','Ana"]
print("Lista inicial: ", nomes)

# Adicionando elementos ao final da lista
nomes.append("Carlos")
print("Após append: ",nomes)

#Insere item na em uma posição específica
#ex: "Fernanda" na posição 1
nomes.insert(1 ,"Fernanda")
print("Após insert: ",nomes)

#Modificando elementos
nomes[2] = "Paulo"
print ("Após modificação: ",nomes)

#Removendo elementos em um índice específico
#ex: elemento no índice 3
del nomes[3]
print("Após del: ", nomes)

#Remove a primeira ocorrência
nomes.remove("Maria")
print("Após remove: ",nomes)

#Remove e retorna o elemento no Índice 2
removido = nomes.pop(2)
print(f"Após pop(removido'{removido}'):",nomes)

#Esvaziando a lista
nomes.clear()
print("Após clear: ",nomes)