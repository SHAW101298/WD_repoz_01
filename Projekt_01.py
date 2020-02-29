print("Hello World") #wersja 3.x
# print "Hello World" #wersja 2.x


# def main():
#     for elem in kolekcja:
#         if costam < 0:
            
imie = "ala"
imie = 0
imie = None

# łańcuchy znaków

imie = "Ala"
print(type(imie))

imie = str("Ala")

# imie = str(100) # "100"
# imie[0] = "O" # nie jest mutowalny

imie = imie.lower()
print(imie)

print("Ala" + " ma " + str(5) + " kotów")
print("Ala ma {}{} kotów".format(5,5))
print("Ala ma {0}{0} kotów".format(5)) # określanie indexu

#f-string
ilosc_kotow= 5
print(f"Ala ma {5}{6} kotów") 
print(f"Ala ma {ilosc_kotow} kotów") 
print(f"{"Ala":>10}")


# Typy Liczbowe

liczba = 1
liczbaf = 4.2
print(type(liczba))
print(type(liczbaf))

print(0.1+0.2 == 0.3)
print(f"{0.1:.32f}")
print(f"{0.2:.32f}")
print(f"{0.3:.32f}")

# Decimal lub zaokrąglanie

liczba = "100"
print(int(liczba))
print(int(liczba,2)) # w systemie dwójkowym

# bin() oct()   hex()   
