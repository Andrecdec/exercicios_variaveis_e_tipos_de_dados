'''
Seção 4 - exercício 8

Leia uma temperatura em Kelvin e apresente-a convertida em graus Celsius.
A fórmula de conversão é: C= K - 273.15, sendo C a temperatura em Celsius
e K a temperatura em Kelvin.

'''

temp_kelvin = float(input('Conversor de temperatura Kelvin-Celsius.\nInsira a temperatura em Kelvin:'))
print (f'A temperartura atual é de {temp_kelvin} Kelvins.')
temp_celsius = temp_kelvin - 273.15
print(f'A temperatura correspondente em graus Celsius é {temp_celsius:.2f}°C.')
#usa-se o :.xf para limitar em x o número de casas decimais,neste caso, duas casas decimais.
       
