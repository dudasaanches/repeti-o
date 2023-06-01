homem_mais_velho = ""
idade_homem_mais_velho = 0
mulheres_menos_20 = 0

for n in range (1,9):
    nome = input("Digite o nome: ")
    s = str(input("Informe o sexo (Informe com  M/F): "))
    i = int(input("Informe a idade: "))
    if s.lower() == "m" and i > idade_homem_mais_velho:
        homem_mais_velho = nome
        idade_homem_mais_velho = i

    if s.upper() == "f" and i < 20:
        mulheres_menos_20 += 1

print(f"\nO homem mais velho é: {homem_mais_velho}")
print(f"Quantidade de mulheres com menos de 20 anos: {mulheres_menos_20}")