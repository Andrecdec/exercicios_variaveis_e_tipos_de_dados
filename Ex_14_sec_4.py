'''
Seção 4 - exercício 14

Leia um ângulo em graus e apresente-o convertido
em radianos. A fórmula de conversão é: r = g*π/180, sendo G o
ângulo em graus, R em radianos e π = 3.14.

'''

g = float(input('Conversor de ângulo em graus para radianos.\nInsira o ângulo em graus:'))
print (f'O ângulo inserido é de {g}°.')
r = g*3.14/180
print(f'Em radianos o ângulo é {r:.2f} rad.')
#usa-se o :.xf para limitar em x o número de casas decimais,neste caso, duas casas decimais.
       
