entrada = []
N = int(input())  # Numero de entrada

for _ in range(N): # Pegando entradas N vezes
    entry = int(input())
    entrada.append(entry) # Adicionando entradas a lista

#Selection sort para colocar os elementos em ordem crescente
entrada.sort()

print(entrada)

# função para contar a quantidade de cada entrada, gerando um dict
"""d = dict.fromkeys(entrada, 0)
for val in entrada:
    d[val] += 1

# expondo Valores
for key, value in d.items():
    print(f"{key} aparece {value} vez(es)")"""