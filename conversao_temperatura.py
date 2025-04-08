'''
Conversão de Temperatura (Celsius para Fahrenheit)
Crie um programa que converta uma temperatura em Celsius para Fahrenheit.
Fórmula: Fahrenheit = (Celsius * 9/5) + 32
'''
temperatura_str = input("Digite a temperatura em Celcius: ")

try:
    temp_ceslcius = float(temperatura_str)
    temp_fahrenheit = (temp_ceslcius * 9/5) + 32
    print("A temperatura em Fahrenheit é: ",temp_fahrenheit)
except ValueError:
    print("Digite uma temperatura válida.")

'''
Conversão de Temperatura (Fahrenheit para Celsius)
Crie um programa que converta uma temperatura em Fahrenheit para Celsius.
Fórmula: Celsius = (Fahrenheit -32) * 5/9
'''

temperatura_str2 = input("Digite a temperatura em Fahrenheit: ")

try:
    temp_fah = float(temperatura_str2)
    temp_cel = (temp_fah -32 ) * 5/9
    print("A temperatura em Celsius é: ", "{:.2f}".format(temp_cel))
except ValueError:
    print("Digite uma temperatura válida.")