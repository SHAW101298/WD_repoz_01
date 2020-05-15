x = input("Podaj dowolna liczbe: ")
x_liczba = int(x)

if x_liczba < 0:
    x_liczba *= -1
    print("X jest ujemne. Wartosc Bezwzgledna to: " + str(x_liczba))