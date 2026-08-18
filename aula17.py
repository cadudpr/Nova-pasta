# if / elif      / else
# se / se não se / se não
# não posso ter else ou elif sozinho, ambos dependem de um if

condicao1 = True
condicao2 = True
condicao3 = True
condicao4 = True

# a primeira que é checada verdadeira, o código dela é executado e o restante é ignorado

if condicao1:
    print('Código para condição 1')
    print('Código para condição 1')
elif condicao2:
    print('Código para condição 2')
elif condicao3:
    print('Código para condição 3')
elif condicao4:
    print('Código para condição 4')
else:
    print('Nenhuma condição foi satisfeita')

if 10  == 10:
    print('Outro if')

print('Fora do if   ')