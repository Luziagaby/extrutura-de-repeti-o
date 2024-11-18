menor_numero = float('inf')

for gaby in range(10):
    numero = float(input(f"Digite o número {gaby + 1}: "))
    if numero < menor_numero:
        menor_numero = numero

print(f"O menor número digitado foi: {menor_numero}")