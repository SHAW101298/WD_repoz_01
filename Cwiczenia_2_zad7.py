#tab = liczby[5]
tab = []
print("Wpisz liczby")

for x in range(0, 5):
    tab.append(float(input(str(x) + ". = ")))

for x in range(0, 5):
    print(str(x) + ". " + str(tab[x]*tab[x]))