def iloczyn_skalarny(A, B):
    """Oblicza iloczyn skalarny dwóch wektorów."""
    return A[0] * B[0] + A[1] * B[1] + A[2] * B[2]

def wspolrzedne_do_wektora(x, y, z):
    """Konwertuje współrzędne do wektora."""
    return [x, y, z]

Ax = int(input("Podaj współczynnik x wektora a: "))
Ay = int(input("Podaj współczynnik y wektora a: "))
Az = int(input("Podaj współczynnik z wektora a: "))
Bx = int(input("Podaj współczynnik x wektora b: "))
By = int(input("Podaj współczynnik y wektora b: "))
Bz = int(input("Podaj współczynnik z wektora b: "))

A = wspolrzedne_do_wektora(Ax, Ay, Az)
B = wspolrzedne_do_wektora(Bx, By, Bz)

print(f"Iloczyn skalarny wektorów A i B wynosi: {iloczyn_skalarny(A, B)}")