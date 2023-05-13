# Dzień 80 Liczby zmiennoprzecinkowe
x = 3.14
y = -0.5
z = 8.0
# Funkcja float przekształca liczbę całkowitą lub łańcuch znaków w liczbę zmiennoprzecinkową
a = float(7)
b = float("3.5")
# Operacje matematyczne na liczbach zmiennoprzecinkowych
suma = x + y
roznica = x - y
iloczyn = x * y
iloraz = x / y
potega = x ** y
# Funkcje wbudowane dla liczb zmiennoprzecinkowych
zaokraglone = round(3.14159, 2) # wynik: 3.14
bezwzgledna = abs(-3.14) # wynik: 3.14
calkowita, reszta = divmod(8.5, 3) # wynik: (2.0, 2.5)
# Pułapki związane z liczbami zmiennoprzecinkowymi
wynik = 0.1 + 0.2
print(wynik) # wynik: 0.30000000000000004
# Funkcja round zaokrągla liczby
wynik = 0.1 + 0.2
print(round(wynik)) # wynik: 0
#Porównywanie liczb
x = 0.1 + 0.2
y = 0.3

print(x == y)
#Tolerancja błędu epsilon

epsilon = 1e-9
print(abs(x - y) < epsilon) # wynik: True

#Zadanie

a = 15.2
b = -4.25

print(a == b)

epsilon = 1e-9
print(abs(a - b) < epsilon)
epsilon = 1e-9
print(abs(a + b) < epsilon)
epsilon = 1e-9
print(abs(a != b) < epsilon)
epsilon = 1e-9
print(abs(a != b) < epsilon)
epsilon = 1e-9
print(abs(a > b) < epsilon)
epsilon = 1e-9
print(abs(a < b) < epsilon)
epsilon = 1e-9
print(abs(a >= b) < epsilon)
epsilon = 1e-9
print(abs(a <= b) < epsilon)
epsilon = 1e-9
print(abs(x ** y) < epsilon)
