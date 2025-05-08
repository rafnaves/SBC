while True:
    G, P = map(int, input().split()) #Leitura dos inteiros
    if G == 0 and P == 0:
        break

    corridas = []
    for _ in range(G): # Função de armazenar os valores para G corridas
        posicoes = list(map(int, input().split()))
        corridas.append(posicoes)

    S = int(input())
    sistemas = []
    for _ in range(S):
        dados = list(map(int, input().split()))
        K = dados[0]
        pontos = dados[1:]
        sistemas.append(pontos)

    # Cálculo da pontuação por sistema
    for sistema in sistemas:
        pontuacao = [0] * P  # índice 0 = piloto 1

        for corrida in corridas:
            for piloto_id, colocacao in enumerate(corrida):
                if colocacao <= len(sistema): # se o piloto chegou numa posição que pontua
                    pontuacao[piloto_id] += sistema[colocacao - 1] 

        max_pontos = max(pontuacao)
        campeoes = [i + 1 for i, pontos in enumerate(pontuacao) if pontos == max_pontos]

        print(*campeoes)
