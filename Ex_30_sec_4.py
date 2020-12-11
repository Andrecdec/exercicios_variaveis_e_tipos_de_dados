'''
Seção 4 - exercício 30

Leia leia um valor em real  e a cotação em dólar.
Em seguida, imprima o valor correspondente em dólares.

'''
valor_real = float(input('Insira aqui o valor em real que você deseja que seja convertido:'))
cotação_dolar = float(input('Agora insira a cotação do dólar de hoje:'))

valor_corresp = valor_real / cotação_dolar
print(f'O valor correspondente em dólares é ${valor_corresp:.2f}.')




       
