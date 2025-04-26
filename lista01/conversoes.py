'''
Verificação de Par ou Ímpar
Crie um programa que verifique se um número é par ou ímpar e imprima o resultado.
'''

print("Vamos verificar se é um número é par ou ímpar!")
num_str = input("Digite um número inteiro: ")

num = 0
try:
    num = int(num_str)
except ValueError:
    print("Você não digitou um número inteiro! Vamos usar o valor padrão 7")
    num = 7

if num % 2 == 0:
    print("É par!")
else:
    print("É impar!")


'''
Conversão de Metros para Centímetros
Crie um programa que converta um valor em metros para centímetros (1 metro = 100 centímetros).
'''

print("Vamos transformar metros em centímetros!")
entrada = input("Digite quantos metros: ")

try:
    metros = float(entrada)
except ValueError:
    print("Valor incorreto! Vamos usar 3m")

if metros > 0:
    print("São ", metros * 100, " centimetros!")

'''
Cálculo do IMC (Índice de Massa Corporal)
Crie um programa que calcule o IMC utilizando o peso (em kg) e a altura (em metros).
Fórmula: IMC = peso / (altura * altura)
'''
print("Vamos calcular o seu IMC!")
peso_str = input("Digite seu peso: ")
altura_str = input("Digite sua altura: ")

try:
    peso = float(peso_str)
    altura = float(altura_str)
except ValueError:
    print("Peso ou altura informados não são válidos.")

imc = peso / (altura * altura)

print("Seu IMC é:")