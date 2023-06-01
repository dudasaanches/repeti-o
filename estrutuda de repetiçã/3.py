mulher = 0
homem = 0

idadeMulheres = 0
idadeHomens = 0

for n in range (1,11):
    s = str(input("Informe o sexo (Informe com M/F): "))
    i = int(input("Informe a idade: "))
    if s.lower() == "f":
        mulher += 1
        idadeMulheres += i
    elif s.lower() == "m":
        homem += 1
        idadeHomens += i

mediamulher = idadeMulheres/mulher
print(f"Idade média das mulheres: {mediamulher}")

mediahomem = idadeHomens/homem
print(f"Idade média dos homens: {mediahomem}")

geral =(idadeMulheres+idadeHomens) / (mulher+homem)
print(f"Idade média do grupo: {geral}")