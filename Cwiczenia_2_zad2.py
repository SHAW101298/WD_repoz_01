import sys

#sys.stdout.write("Podaj 1 wartosc")
#sys.stdout.write("")

#sys.stdout.write("Podaj 2 wartosc")
x = sys.stdin.readline()
y = sys.stdin.readline()

#sys.stdout.write("")

wynik = int(x) * int(y)
tekst = str(wynik)

sys.stdout.write("Wynik = " + tekst)
