'''
Seção 4 - exercício 43

Escreva um programa de ajuda para vendedores . A partir de um valor lido, mostre:

- O total a pagar com desconto de 10%;
- O valor de cada parcela, no parcelamento de 3x sem juros;
- A comissão do vendedor, no caso da venda ser a vista(5% sobre o valor com desconto);
- A comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total).

'''

valor_lido = float(input('Insira aqui o valor total da compra:'))

total_c_desconto = valor_lido - valor_lido*0.1
parcela = valor_lido/3
comissao_vista = 0.05*total_c_desconto
comissao_parcela = 0.05*valor_lido

print(f'O total a pagar com desconto de 10% é R${total_c_desconto:.2f}.')
print(f'O valor de cada parcela, no parcelamento de 3x sem juros é R${parcela:.2f}.')
print(f'A comissão do vendedor, no caso da venda ser a vista é R${comissao_vista:.2f}.')
print(f'A comissão do vendedor, no caso da venda ser parcelada é R${comissao_parcela:.2f}.')

       
