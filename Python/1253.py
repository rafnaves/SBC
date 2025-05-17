CasosDeTeste = int(input()) # Leitura do número de casos de teste
for _ in range(CasosDeTeste): # Loop para cada caso de teste
    String = input()   # Leitura da string
    int1 = int(input()) # Leitura do inteiro

    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                "U", "V", "W", "X", "Y", "Z"]  # Alfabeto
    for i in range(len(String)): # Loop para cada letra da string
        # Verifica se o caractere é um espaço
        if String[i] == " ": # Se for espaço, não faz nada
            continue
        else:
            index = alphabet.index(String[i]) # Encontra o índice da letra no alfabeto
            index = (index - int1) % 26
            String = String[:i] + alphabet[index] + String[i + 1:]

    print(String)