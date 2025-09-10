# criar um sistema que cadastra contatos.
nome = (input("Digite o nome do seu contato: "))
email = (input("Digite o email do seu contatato: "))
tel = input("Digite o telefone do seu contato: ")

with open("Contatos.txt", "w") as result:
    result.write(nome + "|" + email + "|" + "tel")
    result.close()