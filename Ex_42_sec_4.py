'''
Seção 4 - exercício 42

Receba o salário-base de um funcionário. Calcule e imprima o salário a receber,
sabendo-se que esse funcionário tem uma gratificação de 5% sobre o salário-base.
Além disso, ele paga 7% de imposto sobre o salário-base.

'''

salario_base = float(input('Insira aqui o salário-base do funcionário:'))

salario_a_receber = salario_base + salario_base*0.05 - salario_base*0.07
                     
print(f'O funcionário deve receber de salário líquido R${salario_a_receber:.2f}.')

       
