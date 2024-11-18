maiores_de_idade = 0

for luzia in range(20):
    idade = int(input(f"Digite a idade da pessoa {luzia + 1}: "))
    if idade >= 18:
        maiores_de_idade += 1

print(f"O número de pessoas maiores de idade é: {maiores_de_idade}")