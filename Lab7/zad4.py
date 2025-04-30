def iloczyn_skalarny(A, B):
    """Oblicza iloczyn skalarny dwóch wektorów."""
    return A[0] * B[0] + A[1] * B[1] + A[2] * B[2]

def wspolrzedne_do_wektora(x, y, z):
    """Konwertuje współrzędne do wektora."""
    return [x, y, z]

def dlugosc_wektora(A):
    """Oblicza długość wektora."""
    return (A[0]**2 + A[1]**2 + A[2]**2) ** 0.5

def cosinus_wektora(A, B):
    """Oblicza cosinus kąta między dwoma wektorami."""
    iloczyn = iloczyn_skalarny(A, B)
    dlugosc_A = dlugosc_wektora(A)
    dlugosc_B = dlugosc_wektora(B)
    return iloczyn / (dlugosc_A * dlugosc_B)

def iloczyn_wektorowy(A, B):
    """Oblicza iloczyn wektorowy dwóch wektorów."""
    return [
        A[1] * B[2] - A[2] * B[1],
        A[2] * B[0] - A[0] * B[2],
        A[0] * B[1] - A[1] * B[0]
    ]

Ax = int(input("Podaj współczynnik x wektora a: "))
Ay = int(input("Podaj współczynnik y wektora a: "))
Az = int(input("Podaj współczynnik z wektora a: "))
Bx = int(input("Podaj współczynnik x wektora b: "))
By = int(input("Podaj współczynnik y wektora b: "))
Bz = int(input("Podaj współczynnik z wektora b: "))

A = wspolrzedne_do_wektora(Ax, Ay, Az)
B = wspolrzedne_do_wektora(Bx, By, Bz)

print(f"Iloczyn skalarny wektorów A i B wynosi: {iloczyn_skalarny(A, B)}")

dlA = dlugosc_wektora(A)
dlB = dlugosc_wektora(B)
print(f"Długość wektora A wynosi: {dlA}")
print(f"Długość wektora B wynosi: {dlB}")

print(f"Cosinus kąta między wektorami A i B wynosi: {cosinus_wektora(A, B)}")

print(f"Iloczyn wektorowy wektorów A i B wynosi: {iloczyn_wektorowy(A, B)}")