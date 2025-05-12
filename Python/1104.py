while True:
    A, B = map(int, input().split())  # lendo os inteiros 
    if A == 0 and B == 0:             # parando para a entrada 0, 0
        break

    # lendo cartas da alice
    cartasA = set(map(int, input().split()))

    # lendo cartas da beatrix
    cartasB = set(map(int, input().split()))

    # cartas únicas que Alice tem e que Beatriz não tem
    unicas_alice = cartasA - cartasB

    # cartas únicas que Beatriz tem e que Alice não tem
    unicas_beatriz = cartasB - cartasA


    print(min(len(unicas_alice), len(unicas_beatriz)))
