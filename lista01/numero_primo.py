'''
Verificação de Número Primo
Crie um programa que verifique se um número é primo.
Um número é primo se for maior que 1 e não possuir divisores além de 1 e ele mesmo.
Verifique, por exemplo, se 7 é primo.
'''
import math

print("Vamos verificar se um número é primo.")
entrada = input("Digite um número: ")

try:
    num = int(entrada)
except ValueError:
    print("Ops, número inválido! Vamos usar 7 como exemplo!")
    num = 7

eh_primo = True

# Exemplo 1, menos eficiente
# if num <= 1:
#     eh_primo = False
# else:
#     i = 2
#     while i < num:
#         if num % i == 0:
#             eh_primo = False
#             break
#         i += 1

# Exemplo 2, mais eficiente, calculamos a raiz quadrada do número e veririfamos através dela 
if num <= 1:
    eh_primo = False
else:
    for i in range(2, int(math.sqrt(num)) + 1): # Biblioteca math.sqrt() calcula a raiz quadrada de um número
        if num % 2 == 0:
            eh_primo = False
            break

if eh_primo:
    print("É primo.")
else:
    print("Não é primo.")

