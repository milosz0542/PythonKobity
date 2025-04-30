def usun_powtorzenia(lista):
    """Funkcja usuwa powtórzenia z listy"""
    lista_bez_powtorzen = []
    for i in range(len(lista)):
        if lista[i] not in lista_bez_powtorzen:
            lista_bez_powtorzen.append(lista[i])
    return lista_bez_powtorzen

lista = [2, 1, 2, 2, 3, 4, 3, 5, 1, 2, 3, 4, 5]
print(usun_powtorzenia(lista))