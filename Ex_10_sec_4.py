'''
Seção 4 - exercício 10

Leia uma velocidade em km/h (quilomêtros por hora) e apresente-a convertida
em m/s (metro por segundo). A fórmula de conversão é: M=K/3.6, sendo K a
velocidade em km/h e M em m/s.

'''

k = float(input('Conversor de velocidades km/h - m/s.\nInsira a velocidade em Km/h:'))
print (f'A velocidade inserida é de {k} km/h.')
m = k/3.6
print(f'A velocidade correspondente em m/s é {m:.2f} m/s.')
#usa-se o :.xf para limitar em x o número de casas decimais,neste caso, duas casas decimais.
       
