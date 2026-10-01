""" Calculadora com while """
while True:
    print("nummmm")
    sair = input('Quer sair? [s]im: ')
    sair = sair.lower() # converte tudo para MINUSCULO
    sair = sair.startswith("s") # saber com qual letra começa para saber oq fazer

# da pra fazer tudo em uma linha só por exemplo: sair = input('Quer sair? [s]im: ').lower().startswith("s")

    if sair is True:
        break