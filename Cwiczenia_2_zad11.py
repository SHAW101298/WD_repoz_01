a = int(input("Podaj wysokosc diamentu. Liczbe Nieparzysta z Przedzialu 3-9: "))

cntr = int((a+1)/2)

for x in range(1, a+1, 1):
    #print("{:^10}".format('o'*(2*(cntr-abs(cntr-a))-1)))
    print("{:^10}".format('o'*(2*(cntr-abs(cntr-x))-1)))