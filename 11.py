salario_minimo = 850
contagem_menor_salario_minimo = 0
contador = 0

while contador < 5:
    salario = float(input("Digite o salário da pessoa: "))
    if salario < salario_minimo:
        contagem_menor_salario_minimo += 1
        
    contador += 1

print(f"Número de pessoas que recebem menos de um salário mínimo: {contagem_menor_salario_minimo}")
