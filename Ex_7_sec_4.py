'''
Seção 4 - exercício 7

Leia uma temperatura em graus Fahrenheit e apresente-a convertida em Celsius.
A fórmula de conversão é: C=5.0*(F-32.0)/9.0, sendo C a temperatura em Celsius
e F a temperatura em Fahrenheit.

'''

temp_fahrenheit = float(input('Conversor de temperatura graus Fahrenheit-Celsius.\nInsira a temperatura em graus Fahrenheit:'))
print (f'A temperartura atual é de {temp_fahrenheit} °F.')
temp_celsius = 5.0*(temp_fahrenheit-32.0)/9.0
print(f'A temperatura correspondente em graus Celsius é {temp_celsius:.1f}°C.')
#usa-se o :.xf para limitar em x o número de casas decimais,neste caso, apenas uma casa decimal
       
