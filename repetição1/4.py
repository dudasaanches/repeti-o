contagem = 0
for n in range (5,101):
    if n % 7 == 0 and n % 5 != 0:
        contagem +=1
        print(f"Os números são: {n}")
print(f"\nA quantidade é: {contagem}")