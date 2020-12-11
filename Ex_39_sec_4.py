'''
Seção 4 - exercício 39

A importância de R$ 780.000,00 será divida entre três ganhadores de um concurso.
Sendo que da quantia total:

- O primeiro ganhador receberá 46%;
- O segundo receberá 32%;
- O terceiro receberá o restante.

Calcule e imprima a quantia ganha por cada um dos ganhadores.
'''
print('A importância de R$ 780.000,00 será divida entre três ganhadores de um concurso.\nSendo que da quantia total:\n- O primeiro ganhador receberá 46%;\n- O segundo receberá 32%;\n- O terceiro receberá o restante.\nCalcule e imprima a quantia ganha por cada um dos ganhadores.')

total = 780_000.00
primeiro_ganhador = total*0.46
segundo_ganhador  = total*0.32
terceiro_ganhador = total - (primeiro_ganhador + segundo_ganhador)

print(f'O primeiro ganhador ganhará R${primeiro_ganhador:.2f}, \no segundo ganhador ganhará R${segundo_ganhador:.2f} \ne o terceiro ganhador ganhará R${terceiro_ganhador:.2f}.')



       
