nome = input("Digite seu nome: ")
email = input("Digite seu e-mail: ")

with open("Pessoa.txt", "a") as arquivo:
    arquivo.write(nome + " | " + email + "\n")
