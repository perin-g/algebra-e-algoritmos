'''
Cálculo da Área de um Círculo
Crie um programa que calcule a área de um círculo, usando pi = 3.14 e a fórmula: Área = pi * (raio * raio).
'''
pi: float = 3.14

print("Vamos calcular a área de um círculo, digite o raio!")
raio_str = input("Raio: ")

try:
    raio = float(raio_str)
except ValueError:
    print("Ops! Valor inválido, usaremos 10 como padrão!")
    raio = 10

area = pi * (raio * raio)

print("Á área é: ", area)


'''
Cálculo do Fatorial
Crie um programa que calcule o fatorial de um número inteiro positivo (por exemplo, 5!) utilizando um loop (for ou while).
'''

print("Vamos calcular o fatorial de um número!")
num_str = input("Digite um número inteiro maior que zero: ")

try:
    num = int(num_str)
    if num < 0:
        raise ValueError # Forçando uma exceção
except ValueError:
    print("Parece que você não digitou um número inteiro maior que zero. Neste caso vamos calcular o fatorial de 5.")
    num = 5

fatorial = 1
while num >= 1:
    fatorial *= num
    num -= 1

print("O fatorial é: ", fatorial)