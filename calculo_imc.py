nome = input("Informe seu nome: ")
altura = float(input("Informe sua altura em centímetros: ")) / 100
peso = float(input("Informe seu peso em quilogramas: "))

imc = peso / (altura ** 2)

categoria = ""
if imc < 18.5:
    categoria = "Abaixo do Peso (Pegue suplementos do Cariani)"
elif 18.5 <= imc <= 24.9:
    categoria = "Peso Ideal (Para Bens)"
elif 25.0 <= imc <= 29.9:
    categoria = "Sobrepeso"
elif 30.0 <= imc <= 34.9:
    categoria = "Obesidade Grau 1"
elif 35.0 <= imc <= 39.9:
    categoria = "Obesidade Grau 2"
else:
    categoria = "Obesidade Grau 3 (Dr. Nowzaradan te espera)"

print(f"Olá, {nome}! Seu IMC é {imc:.2f} e sua categoria é: {categoria}")
