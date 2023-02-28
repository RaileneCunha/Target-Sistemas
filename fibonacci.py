n = int(input("Digite um valor: "))
valor1 = 0
valor2 = 1
soma = 0
print('{} -> {}'.format(valor1, valor2), end='')
cont = 3
while cont <= n:
    soma = valor1 + valor2
    print(' -> {}'.format(soma), end='')
    valor1 = valor2
    valor2 = soma
    cont += 1
if(n==0 or n==1):
    print('\nO número faz parte da sequência de Fibonacci!')
elif(n==soma):
    print('\nO número faz parte da sequência de Fibonacci!')
else:
    print('\nO número não faz parte da sequência de Fibonacci!')