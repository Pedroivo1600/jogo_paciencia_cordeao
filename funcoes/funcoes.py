def cria_baralho():
    i = 2
    lista = []
    lista.append('J♠')
    lista.append('J♥')
    lista.append('J♦')
    lista.append('J♣')
    lista.append('A♠')
    lista.append('A♥')
    lista.append('A♦')
    lista.append('A♣')
    lista.append('K♠')
    lista.append('K♥')
    lista.append('K♦')
    lista.append('K♣')
    lista.append('Q♠')
    lista.append('Q♥')
    lista.append('Q♦')
    lista.append('Q♣')
    while i <= 10:
        lista.append(str(i)+'♠')
        lista.append(str(i)+'♥')
        lista.append(str(i)+'♦')
        lista.append(str(i)+'♣')
        i += 1
    return lista

def extrai_naipe(x):
    if len(x) == 2:
        return x[1]
    else:
        return x[2]

def extrai_valor(x):
    if len(x)==2:
        return x[0]
    else:
        return x[0] + x[1]

def lista_movimentos_possiveis(lista, x):
    if x == 0:
        return []
    if x <= 2 and x > 0:
        if extrai_valor(lista[x]) == extrai_valor(lista[x-1]):
            return [1]
        if extrai_naipe(lista[x]) == extrai_naipe(lista[x-1]):
            return [1]
        else:
            return []
    if extrai_valor(lista[x]) == extrai_valor(lista[x-1]) and extrai_valor(lista[x]) == extrai_valor(lista[x-3]) or extrai_valor(lista[x]) == extrai_valor(lista[x-1]) and extrai_naipe(lista[x]) == extrai_naipe(lista[x-3]) or extrai_naipe(lista[x]) == extrai_naipe(lista[x-1]) and extrai_valor(lista[x]) == extrai_valor(lista[x-3]) or extrai_naipe(lista[x]) == extrai_naipe(lista[x-1]) and extrai_naipe(lista[x]) == extrai_naipe(lista[x-3]) and x>2:
        return [1, 3]
    if extrai_naipe(lista[x]) == extrai_naipe(lista[x-1]) and x > 2:
        return [1]
    if extrai_naipe(lista[x]) == extrai_naipe(lista[x-3]) and x > 2:
        return [3]
    if extrai_valor(lista[x]) == extrai_valor(lista[x-1]) and x > 2:
        return [1]
    if extrai_valor(lista[x]) == extrai_valor(lista[x-3]):
        return [3]
    else:
        return []

def empilha(baralho, origem, destino):
    baralho.pop(destino)
    baralho.insert(destino, baralho[origem-1])
    x = baralho.index(baralho[origem], destino+1)
    baralho.pop(x)
    return baralho
