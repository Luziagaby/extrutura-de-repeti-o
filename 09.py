soma_idades = 0
idade_mais_nova = float('inf') # ese inf siguinifica enfinito emprogramação
idade_mais_velha = float('-inf')
nome_mais_novo = ""
nome_mais_velho = ""

for i in range(10):
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    
    soma_idades += idade
    
    if idade < idade_mais_nova:
        idade_mais_nova = idade
        nome_mais_novo = nome
        
    if idade > idade_mais_velha:
        idade_mais_velha = idade
        nome_mais_velho = nome

media_idades = soma_idades / 10
print(f"A pessoa mais nova é {nome_mais_novo} com {idade_mais_nova} anos.")
print(f"A pessoa mais velha é {nome_mais_velho} com {idade_mais_velha} anos.")
print(f"A média das idades é {media_idades:.2f}.")
