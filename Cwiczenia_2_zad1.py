a = input("Podaj Tekst: ")
#a = "Dowolny tekst ktory tak poprostu sam sie pojawil. Przysiegam, nie wiem jak to sie stalo"

#print("Wczytany tekst: " + a)

spc = 0
dlugosc = len(a)
for x in range(0, dlugosc):
    if a[x] == " ":
        spc = spc + 1
print(spc)