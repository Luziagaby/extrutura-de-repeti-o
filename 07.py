contador = 0

while contador < 15:
    numero = int(input(f"Digite o número {contador + 1}: "))
    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    contador += 1