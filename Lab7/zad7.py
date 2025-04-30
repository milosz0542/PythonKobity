import numpy as np

def analiza(lista):
    krotka = ()
    krotka += (len(lista),)
    krotka += (np.mean(lista),) # albo można samemu obliczyć, ja jestem zbyt leniwy
    krotka += (max(lista),)
    krotka += (np.std(lista),)
    return krotka

# Przykładowe użycie
lista = [5, 6, 8, 9, 11, 12]
wynik = analiza(lista)
print(wynik)
print(f"Liczba elementów: {wynik[0]}")
print(f"Średnia: {wynik[1]}")
print(f"Maksimum: {wynik[2]}")
print(f"Odchylenie standardowe: {wynik[3]}")