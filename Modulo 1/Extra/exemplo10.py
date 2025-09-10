nome = input("Digite seu nome: ")
email = input("Digite seu e-mail: ")

arquivo = open("Pessoa.txt", "a")
arquivo.write(nome + " | " + email + "\n")
arquivo.close()
