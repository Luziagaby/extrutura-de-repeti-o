soma = 0
contador = 0  

while contador < 10:
    numero = float(input(f"Digite o número {contador + 1}: "))
    soma += numero
    contador += 1
media = soma / 10

print(f"A média aritmética dos 10 números é: {media}")
