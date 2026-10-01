'''
Iterando string com while
'''

nome = "Carlos Eduardo"


i = 0
while i < len(nome):
    if i < len(nome) - 1: 
     print(nome[i], end="*")
    else:
       print(nome[i])
    i += 1

    # o que ele fez 

nome = 'Maria Helena'  # Iteráveis

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)