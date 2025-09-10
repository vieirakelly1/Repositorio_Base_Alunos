nome = input("Digite o nome do paciente: ")
peso = float(input("Digite o peso em quilogramas(kg):  "))
altura = float(input("Digite a altura em metros(m): "))
IMC = peso / (altura*altura)
print(f"Indice de massa corporal: {IMC:.2f}")


if IMC < 18.5:
    print (nome, f"apresenta índice de massa corporal: {IMC:.2f}","e Classificação: Abaixo do peso.")

elif IMC >=18.5 and IMC <=24.9:
    print (nome, f"apresenta índice de massa corporal: {IMC:.2f}","e Classificação: Peso normal.")

elif IMC >=25.0 and IMC <=29.9:
    print(nome, f"apresenta índice de massa corporal: {IMC:.2f}","e Classificação: Sobrepeso.")

elif IMC >=30.0 and IMC <=34.9:
    print(nome, f"apresenta índice de massa corporal: {IMC:.2f}","e Classificação: Obesidade 1º grau.")

elif IMC >=35.0 and IMC <=39.9:
     print(nome, f"apresenta índice de massa corporal: {IMC:.2f}","e Classificação: Obesidade 2º grau.")

else:
    print(nome, f"apresenta índice de massa corporal: {IMC:.2f}","e Classificação: Obesidade 3º grau.")
