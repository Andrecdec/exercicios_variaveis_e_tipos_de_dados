'''
Seção 4 - exercício 6

Leia uma temperatura em graus Celsius e apresente-a convertida em Fahrenheit.
A fórmula de conversão é: F=C*(9.0/5.0) + 32.0, sendo F a temperatura
em Fahrenheit e C a temperatura em Celsius.

'''

temp_celsius = float(input('Conversor de temperatura graus Celsius-Fahrenheit.\nInsira a temperatura em graus Celsius:'))
print (f'A temperartura atual é de {temp_celsius} °C.')
temp_fahrenheit = temp_celsius * (9.0/5.0) + 32.0
print(f'A temperatura correspondente em Fahrenheit é {temp_fahrenheit:.1f}°F.')
#usa-se o :.xf para limitar em x o número de casas decimais, neste caso, apenas uma casa decimal
       
