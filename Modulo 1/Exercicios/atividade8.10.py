# Dada a lista [10, 20, 30, 40, 50]:
# 1. Adicione 60 no final.
# 2. Insira 15 na posição 1.
# 3. Remova o elemento 30.
# 4. Remova o último elemento e guarde-o em uma variável.

dezenas = [10,20,30,40,50]
dezenas.insert(1,15)
dezenas.insert(5,60)
dezenas.remove(30)
d = dezenas.pop(5)

print(dezenas)