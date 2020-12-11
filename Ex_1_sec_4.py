'''
Seção 4 - exercício 1 (modificado)

Faça um programa que leia um número inteiro e o imprima.

Modifiquei um pouco o código para caso o número inputado não seja um inteiro.

'''

numero_float = float(input('Qual é o seu número inteiro?'))
numero_int = int(float(numero_float))
diferença = numero_int - numero_float

while diferença != 0:
       numero_float = float(input('Este número não é inteiro. Por favor insira um número inteiro:'))
       numero_int = int(float(numero_float))
       diferença = numero_int - numero_float
print(f'Seu número inteiro é {numero_int}')
