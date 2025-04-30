def po_bozemu(lista):
    print(lista)
    print(f"Największa liczba na liście to {max(lista)}")
    print(f"Ostatni element tablicy to: {lista.index(N-1)}")
    print(f"Suma elementów tablicy to: {sum(lista)}")
    print(f"Średnia elementów tablicy to: {sum(lista)/N}") # Lub wykorzystując bibliotekę numpy - np.mean(lista)

def max_lista(lista):
    max_value = lista[0]
    for i in range(1, len(lista)):
        if lista[i] > max_value:
            max_value = lista[i] # Jeśli jakiś element jest większy od max_value, to go zamieniamy
    return max_value

def suma_lista(lista):
    suma = 0
    for i in range(len(lista)):
        suma += lista[i] # += to zamiennik suma = suma + lista[i]
    return suma

def nie_po_bozemu(lista):
    print(lista)
    print(f"Największa liczba na liście to {max_lista(lista)}")
    print(f"Ostatni element tablicy to: {lista[-1]}") # Ale to akurat jest zrobione po bożemu
    print(f"Suma elementów tablicy to: {suma_lista(lista)}")
    print(f"Średnia elementów tablicy to: {suma_lista(lista)/N}")

# Przykładowe użycie
N = 20

lista = []
for i in range(N):
    lista.append(int(input(f"Podaj liczbę {i+1}: ")))

po_bozemu(lista)
nie_po_bozemu(lista)