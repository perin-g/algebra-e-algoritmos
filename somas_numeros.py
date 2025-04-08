'''
Soma de Dois Números
Crie um programa que some dois números (utilize variáveis para armazená-los) e exiba o resultado.
'''

a_str = input("Digite o primeiro número: ")
b_str = input("Digite o segundo número: ")

try:
    a = int(a_str)
    b = int(b_str)
except ValueError:
    print("Use apenas números inteiros")

print("A soma dos números é: ", a + b)

'''
Média de Três Números
Crie um programa que calcule a média de três números e exiba o resultado.
'''

print("\nVamos calcular a média de 3 números")
num1_str = input("Primeiro número: ")
num2_str = input("Segundo número: ")
num3_str = input("Terceiro número: ")

try:
    num1 = float(num1_str)
    num2 = float(num2_str)
    num3 = float(num3_str)
except ValueError:
    print("Ops, você precisa digitar números")

media = (num1 + num2 + num3) / 3

print("A média é: ", "{:.2f}".format(media))

'''
Maior Número Entre Dois
Crie um programa que, utilizando duas variáveis, determine qual dos dois números é o maior e exiba-o.
'''
print("\nVamos descobrir qual número inteiro é maior")
n1_str = input("Digite o primeiro número: ")
n2_str = input("Digite o segundo número: ")

try:
    n1 = int(n1_str)
    n2 = int(n2_str)
except ValueError:
    print("Ops, você precisa digitar números")

if n1 > n2:
    print("O maior número é: ", n1)
else:
    print("O maior número é: ", n2)