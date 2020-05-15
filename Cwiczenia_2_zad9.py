liczba = input("Podaj Liczbe Wielocyfrową: ")
count = len(liczba)

wynik = 0

#for i in range(0, count):
#    wynik += int(liczba[i])

i = 0
while i < count:
    wynik += int(liczba[i])
    i += 1
print("wynik = " + str(wynik))