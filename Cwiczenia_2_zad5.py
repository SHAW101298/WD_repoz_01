a = input("Podaj a: ")
b = input("Podaj b: ")
c = input("Podaj c: ")
a = int(a)
b = int(b)
c = int(c)

if a > 0 or a <= 10:
    print("a zawiera sie w przedziale 0-10")
else:
    print("a nie zawiera sie w przedziale 0-10")

if a>b:
    print("a jest wieksze od b")
else:
    print("a jest mniejsze lub rowne b")
    pass
if b>c:
    print("b jest wieksze od c")
else:
    print("b jest mniejsze lub rowne c")
    pass