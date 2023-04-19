n = int(input("Entre com o um inteiro numero: "))
soma = 0
cont = 0
for i in range(n, 200 + n):
    soma += i%3
    cont += 1
    print(f"{cont}: {i}/3=r{i%3} q{i//3}")
print(f"Soma dos resto é: {soma}")
