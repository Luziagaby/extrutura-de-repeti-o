votos_candidato1 = 0

votos_candidato2 = 0

for pricila in range(10):
    voto = int(input("Vote no candidato (1 ou 2): "))
    if voto == 1:
        votos_candidato1 += 1
    elif voto == 2:
        votos_candidato2 += 1

if votos_candidato1 > votos_candidato2:
    print("Candidato 1 ganhou a eleição!")
elif votos_candidato2 > votos_candidato1:
    print("Candidato 2 ganhou a eleição!")
else:
    print("A eleição terminou em empate!")
