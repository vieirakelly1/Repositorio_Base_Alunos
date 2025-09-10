def operacao(n1,n2,n3):
    if n2 == '+':
        print(n1+n3)
    elif n2 == '-':
        print(n1-n3)
    elif n2 == '*':
        print(n1*n3)
    elif n2 == '/':
        print(n1/n3)

def periodo(nome,horario):
    if horario >"18:00":
        print("Boa noite ",nome)

    elif horario >= "12:00":
        print("Boa tarde ",nome)
    else:
        print("Bom dia ",nome)

def validacao(senha,createSenha):

    if senha == createSenha:
        print("Validação de senha confirmada.")
    else:
        print("Senha não confere.")

def classificar_numero(numero):
    if numero >=10 or numero <=100:
        return "entre 10 e 100"
    elif numero >= 0 or numero <= 10:
        return "entre 0 e 10"
    elif numero < 0:
        return "numero negativo"
    else:
        return "maior que 100"
    
    