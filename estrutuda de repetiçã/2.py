cliente = int(input("Quantidade de clientes analisados: "))
soma = 0

for n in range (1,cliente+1):
    t = float(input("Informe a temperatura: "))
    soma += t
    if t < 37.2:
        print("Temperatura normal")
    elif t >= 37.3 and t < 38:
        print("Estado Febril")
    elif  t >= 38 and t <= 39:
        print("Com febre")
    elif  t >= 39:
        print("Com febre alta")

media = soma/cliente
print(f"Pessoas analisadas: {cliente}")
print(f"Media de temperatura: {media}")