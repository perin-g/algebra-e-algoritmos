'''
Contagem Regressiva
Crie um programa que faça uma contagem regressiva de um número dado (por exemplo, 5) até 0, imprimindo cada número.
'''
print("Vamos fazer uma contagem regressiva!")
n_str = input("Digite um número inteiro: ")

try:
    n1 = int(n_str)
except ValueError:
    print("Ops, valor inválido! Vamos usar 5 como exemplo!")
    n1 = 5

while n1 >= 0:
    print("Estamos em: ", n1)
    n1 -= 1

'''
Contagem Crescente
Crie um programa que imprima os números de 1 a 10 usando um loop 'for'.
'''

print("\nOlá, esse programa irá contar até 10")

for i in range(1, 11):
    print(i)

'''
Tabuada de um Número
Crie um programa que imprima a tabuada de um número (por exemplo, a tabuada do 3) para os números de 1 a 10.
'''

print("\nOlá, vamos calcular a tabuáda de um número!")
num_str = input("Digite um número: ")

try:
    n2 = int(num_str)
except ValueError:
    print("Ops, valor inválido! Vamos usar 3 como exemplo!")
    n2 = 3

for i in range (1, 11):
    print(n2, "x", i, "=", n2 * i)

'''
Cálculo de Potência (Sem usar o operador de potência)
Crie um programa que calcule a potência de um número, sem usar o operador **.
Por exemplo, calcule 2 elevado a 4 utilizando um loop.
'''

print("\nVamos calcular a potência de um número!")
n3_str = input("Digite um número: ")

try:
    n3 = int(n3_str)
except:
    print("Ops, valor inválido! Vamos usar 3 ao cubo como exemplo!")
    n3 = 3

potencia = 1

for i in range(1, n3+1):
    potencia *= i

print("A potência é: ", potencia)
