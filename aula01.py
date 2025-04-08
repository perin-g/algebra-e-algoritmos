'''
# 1. Variáveis
print("=== Seção1: Variáveis, atribuições")

# Atribuição simples sem anotação de tipo (forma comum)
a = 10
b = 20

print("Atribuição simples: a =", a, "e b =", b)

# É possível utilizar anotações de tipo para:
# Melhorar a legibilidade
# Serve como documentação
# Ajuda a depuração

c: int = 30
d: int = 40

print("Atribuição simples: c =", c, "e d =", d)

# Atribuição múltipla (chain assignment).
# Definir x, y e z com o mesmo valor
x = 5
y = 5
z = 5
#Simplificando:
x = y = z = 5

# Atribuição múltipla com diferentes valores
nome, idade = "Maria", 30

print("O nome é:", nome, "E a idade é", idade)

# Atribuição composta (incremento)
contador = 0
contador += 1
print("Contador:", contador)

# Atribuição via input do usuário
# Todos os inputs retornam uma String
entrada_str = input("Digite um número inteiro: ")
print("Como String:", entrada_str)

## 2. Conversões

#entrada_str que antes era string "2" e convertendo para int 2
#try é uma estrutura para testar e tratar erros
try:
    numero = int(entrada_str)
    print("Conversão:",numero)
except ValueError:
    print("Erro: A conversão falhou")

# Exemplo com exceção genérica
try:
    numero_generico = int(entrada_str)
except Exception as e:
    print("Exceção genérica: ",e)
quebrado
# Conversão para float
# 1 - Receba uma string do usuário
# 2 - Converta a entrada para float dentro do try catch
# 3 - Trate a excecao com Value Error
entrada_float = input("Digite um número decimal: ")

try:
    valor_decimal = float(entrada_float)
    print("O número é: ", valor_decimal)
except ValueError as e:
    print("Erro: a conversão falhou")


### 3. Operadores aritiméticos e relacionais
num1 = 15
num2 = 4

#Operadores aritiméticos
soma = num1 + num2
subtração = num1 - num2
multiplicação = num1 * num2
divisao = num1 / num2
divisao_inteira = num1 // num2 #Descarta a parte decimal
resto_divisao = num1 % num2 #Resto da divisão
potencia = num1 ** num2 #num1 elevado a num2

# Operadores relacionais
# Elementos que comparam valores e retornam true ou false
print("15 é maior que 4?", num1 >= num2) #Compara se é maior ou igual
print("15 é igual a 4?", num1 == num2) #Compara se duas variáveis são iguais
print("15 é igual a 4?", num1 != num2) #Compara se duas variáveis são diferentes


### 4. Estruturas condicionais
# 1 - Receba um número do usuário
# 2 - Verifique se o número é par ou impar cmo um if/else e print

num3 = input("Digite um número inteiro: ")

try:
    numero_convertido = int(num3)

    if numero_convertido % 2 == 0:
        print("O número digitado é par")
    else:
        print("O número digitado é impar")
except Exception as e:
    print("Ocorreu um erro!", e)

# Receba a idade do usuário e valide se é maior ou menor de idade

str_idade = input("Digite sua idade: ")

try:
    idade = int(str_idade)

    if idade >= 18:
        print("Você é maior de idade")
    else:
        print("Você é menor de idade")
except Exception as e:
    print("Ocorreu um erro!", e)


### 5. Estruturas de repetição
# A função range() gera uma sequencia de numeros
# range(stop)
for i in range(5):
    print("i = ", i)

# range(start, stop)
# Fazer um for que começa em 3 e que termina em 7
for i in range(3,8):
    print("i = ", i)

# range(start, stop, step)
# Inicie em 10 e diminua 2 a cada interação parando antes de atingir -1

for i in range(10, -1, -2):
    print("i = ", i)

# Loop While
# input do usuário
# Converter a string digitada em int
# Se deu problema na conversão, sete 5 como padrão
# While
str_num = input("Digite um número: ")

try:
    num4 = int(str_num)
except ValueError:
    print("Valor inválido, atribuído valor padrão 5")
    num4 = 5

while num4 >= 0:
    print("Contador: ", num4)
    num4 -= 1

print("Loop finalizado")


print("\n Menu \n")
print("Opções")
print("1 - Somar dois números")
print("2 - Subtrair dois números")
print("3 - Sair")
opcao = 0
'''

while opcao != 3:
    opcao_str = input("Digite o número da opção: ")
    try:
        opcao = int(opcao_str)
    except ValueError:
        print("Opcão inválida, digite um número.")
        continue #Reinicia o loop se a conversão falhar
    
    if opcao == 1:
        a_str = input("Digite o primeiro número: ")
        b_str = input("Digite o segundo número: ")

        try:
            a = int(a_str)
            b = int(b_str)
        except ValueError:
            print("Use apenas números inteiros")
            continue

        print("A soma dos números é: ", a + b)
    elif opcao == 2:
        a_str = input("Digite o primeiro número: ")
        b_str = input("Digite o segundo número: ")

        try:
            a = int(a_str)
            b = int(b_str)
        except ValueError:
            print("Use apenas números inteiros")
            continue

        print("A subtração dos números é: ", a - b)
    elif opcao == 3:
        print("Programa encerrado!")
    else:
        print("Opção inválida")

## Formatação String
nome_usuario = input("Digite seu nome: ")
# strip() Remove espaços em branco do começo ao fim da string
# EX:"          João da                    Silva" >>>"João da Silva"
# title() Converte a primeira letra de cada palavra para maiúscula
nome_formatado = nome_usuario.strip().title()

print(nome_formatado)