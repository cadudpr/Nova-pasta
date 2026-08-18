nome = 'Cadu'
altura = 1.90
peso = 85
imc = peso / (altura * altura)

# "f-strings" são uma forma de formatar strings no Python, permitindo a inclusão de expressões dentro de chaves {}. Elas são precedidas pela letra 'f' antes das aspas da string.

linha_1 = f'{nome} tem {altura:.2f} de altura, pesa {peso} e seu IMC é de {imc:.2f}'

print(linha_1)

print(nome, 'tem', altura, 'de altura, pesa',peso,'seu IMC é de' , imc)