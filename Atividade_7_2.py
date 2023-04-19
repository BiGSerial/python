fatorial = int(input('Entre com o Numero a fatorial: '))
n = 1
for i in range(fatorial):
    n *= (fatorial - i)

print(f"{fatorial}! é: {n}")