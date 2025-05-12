while True:
    # lendo o número de bancos (B) e o número de transações (N)
    B, N = map(int, input().split())

    # condição de parada
    if B == 0 and N == 0:
        break

    # lendo as reservas iniciais dos bancos
    reservas = list(map(int, input().split()))

    # processando as N transações
    for _ in range(N):
        devedor, credor, valor = map(int, input().split())

        # atualizando os saldos dos bancos
        reservas[devedor - 1] -= valor  # Banco devedor perde dinheiro
        reservas[credor - 1] += valor   # Banco credor ganha dinheiro

    # verificando se algum banco ficou com saldo negativo
    if all(reserva >= 0 for reserva in reservas):
        print("S")  # todos os bancos podem pagar suas dívidas
    else:
        print("N")  # algum banco ficou insolvente
