'''
Seção 4 - exercício 36

Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro.
O volume de um cilindro circular é calculado por meio da seguinte fórmula:
V = π * raioˆ2 * altura, onde π = 3.141592.

'''
altura = float(input('Cálculo do volume do cilindro a partir do raio e da altura.\nInsira aqui a altura do cilindro:'))
raio = float(input('Agora insira o raio do cilindro:'))

volume = 3.141592 * (raio **2)* altura
print(f'O volume tem {volume:.2f} unidades cúbicas de medida.')




       
