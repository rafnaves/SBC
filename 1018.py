valor = int(input())

print(valor)

notas = [100, 50, 20, 10, 5, 2, 1]

for nota in notas:
    qtd = valor // nota
    print(f"{qtd} nota(s) de R$ {nota},00")
    valor = valor % nota
