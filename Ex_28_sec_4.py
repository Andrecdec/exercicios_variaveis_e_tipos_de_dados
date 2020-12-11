'''
Seção 4 - exercício 28

Faça a leitura de três valores e apresente como resultado
a soma dos quadrados dos três valores lidos.

'''
valor_1 = float(input('Insira 3 valores diferentes. \nO resultado será a soma dos quadrados dos três valores.\nInsira aqui o primeiro valor:'))
valor_2 =float(input('Agora insira o segundo:'))
valor_3 =float(input('Por fim, insira o terceiro:'))

resultado = valor_1**2 + valor_2**2 + valor_3**2
print(f'O resultado é {resultado:.2f}, arredondado com duas casas decimais.')




       
