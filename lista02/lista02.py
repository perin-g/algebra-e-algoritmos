
# Tarefa 01
print("Vamos calcular!")
entrada1 = input("Digite o primeiro valor: ")
entrada2 = input("Digite o segundo valor: ")

try:
    num1 = float(entrada1)
    num2 = float(entrada2)
except ValueError:
    print("Você não digitou um número! Vamos usar como padrão 10 e 2")
    num1, num2 = 10, 2

operacao = input("Digite qual operação deseja realizar, apenas símbolos, + (Soma), - (Subtração), * (Multiplicação), / (Divisão): ")

if operacao == "+":
    resultado = num1 + num2
    print("O resultado é: ", resultado)
elif operacao == "-":
    resultado = num1 - num2
    print("O resultado é: ", resultado)
elif operacao == "*":
    resultado = num1 * num2
    print("O resultado é: ", resultado)
elif operacao == "/":
    if num2 == 0:
        print("Não é possível dividir por 0.")
        exit()
    else:
        resultado = num1 / num2
        print("O resultado é: ", resultado)
else:
    print("Operação inválida!")

# Tarefa 02
import random
num_secret = random.randint(1, 50)

print("\nJogo de Adivinhação!\nVocê tem 5 tentativas para adivinhar o número secreto.\nÉ um número entre 1 e 50!")

for i in range(5):
    num_str = input("Digite um número: ")

    try:
        num = int(num_str)
    except ValueError:
        print("Digite um número inteiro:")
        continue
    
    if num > num_secret:
        print("Palpite acima do número secreto")
    elif num < num_secret:
        print("Palpite abaixo do número secreto")
    elif num == num_secret:
        print("Você adivinhou o número secreto!")
        exit()

# Tarefa 03
print("Vamos contar números Pares e Ímpares!\nDigite 10 números: ")

contador_par = 0
contador_impar = 0

for i in range(1, 11):
    print("Digite o ", i, " número: ")
    entrada = input()

    try:
        numero = int(entrada)
    except ValueError:
        print("Valor incorreto digitado, será tratado como zero.")
        numero = 0

    if numero % 2 == 0:
        contador_par += 1
    else:
        contador_impar += 1

print("O total de números pares foi: ", contador_par, "\nO total de números ímpares foi: ", contador_impar)

# Tarefa 04
print("Vamos calcular a média!")
qtdNotas_str = input("Digite a quantidade de notas a serem ")

try: 
    qtdNotas = int(qtdNotas_str)
except ValueError:
    print("Valor incorreto digitado, usando o valor padrão 2")
    qtdNotas = 2

media = 0
for i in range(qtdNotas):
    print("Digite a ", i + 1, " nota")
    nota_str = input()
    try: 
       nota = float(nota_str)
    except:
        print("Valor inválido digitado, usando valor padrão zero")
        nota = 0
    media += nota

media = media / qtdNotas
if media >= 7:
    print("A média é: ", "{:.2f}".format(media), ". Aprovado!")
else:
    print("A média é: ", "{:.2f}".format(media), ". Reprovado!")


# Tarefa 05
print("Vamos calcular o desconto.")
preco_str = input("Digite o preço do produto: ")
percentual_str = input("informe o percentual do desconto: ")

try:
    preco = float(preco_str)
    percentual = float(percentual_str)
except ValueError:
    print("Valores incorretos digitados, por gentileza inicie o programa novamente.")

desconto = preco * (percentual / 100)
preco_final = preco - desconto

print("Preço final: ", preco_final)

# Tarefa 06
print("Conversor de unidades.")
medida_str = input("Digite o valor da unidade métrica: ")
opcao_str = input("Para converter metros para centímetros digite 1, para converter quilômetros para metros digite 2: ")

try:
    opcao = int(opcao_str)
    medida = float(medida_str)
except ValueError:
    print("Valores incorretos digitados, por gentileza inicie o programa novamente.")

if opcao == 1:
    conversao = medida * 100
    print("São: ", conversao, " centimetros.")
elif opcao == 2:
    conversao = medida * 1000
    print("São: ", conversao, " metros")
else:
    print("Opção inválida. Programa encerrado")

# Tarefa 07
print("Vamos verificar quantos números são positivos, negativos ou zero")

contador_positivo = 0
contador_negativo = 0
contador_zero = 0

while True:
    entrada = input("Digite um número, para sair digite 'sair': ")

    if entrada == "sair":
        break

    try:
        num = float(entrada)
    except ValueError:
        print("Valor inválido, usando o padrão zero")
        num = 0
    
    if num > 0:
        contador_positivo += 1
    elif num < 0:
        contador_negativo += 1
    else:
        contador_zero += 1

print("O total de números positivos é: ", contador_positivo, "\nO total de números negativos é: ", contador_negativo, "\nO total de zeros é: ", contador_zero)

# Tarefa 08
print("Vamos calcular a Área e Perímetro de um Retângulo.")
lagura_str = input("Digite a largura do triângulo: ")
altura_str = input("Digite a altura do triângulo: ")

try:
    lagura = float(lagura_str)
    altura = float(altura_str)
except ValueError:
    print("Valor incorreto, pro gentileza reinicie o programa")

area = lagura * altura
perimetro = 2 * (lagura + altura)

print("A Área é: ", area, "\nO perímetro é: ", perimetro)

#Tarefa 09
print("Vamos converter a idade para Dias, Semanas e Meses")
idade_str = input("Digite sua idade: ")

idade = 0
try:
    idade = int(idade_str)
except ValueError:
    print("Idade informada inválida, vamos usar como padrão 28 anos!")
    idade = 28

if idade < 0:
    print("A idade não pode ser negativa. Por gentileza reinicie o programa.")
    exit()

idade_dias = idade * 365
idade_semanas = idade * 52
idade_anos = idade * 12

print("Você viveu aproximadamente por:\n", idade_dias, " dias.\n", idade_semanas, " semanas.\n", idade_semanas, " anos.")

# Tarefa 10
print("Simulador de conta bancária")
saldoInicial_str = input("Digite o saldo inicial: ")
deposito_str = input("Digite o valor do depósito: ")
saque_str = input("Digite o valor do saque: ")

try:
    saldoInicial = float(saldoInicial_str)
    deposito = float(deposito_str)
    saque = float(saque_str)
except ValueError:
    print("Valor inválido, programa encerrado")
    exit()

saldo = saldoInicial + deposito

if saque <= saldo:
    saldo -= saque
    print("Saque realizado! Saldo atual: ", saldo)
else:
    print("Saldo insuficiente!")