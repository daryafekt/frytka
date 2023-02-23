zmienna = "  hdgfcjFYUKHYFhdguytdrJJFJHDTFJGDGXtst"
print(zmienna.upper()) #litery robia sie wieksze
print(zmienna.lower()) #litery robia sie mniejsze
print(zmienna.title()) #pierwsza litera, wielka reszta male
print(zmienna.lstrip()) #obcina po lewej(rstrip - po prawej)
print(zmienna.find("JJF")) #znajdz
print(zmienna.replace("H","O")) #zamiana znakow na inne
print("H" in zmienna)#czy H jest w zmienna
print("G" not in zmienna)#czy G nie ma w zmienna

print(10/3)
print(10//3)#zaokraglic do calosci
print(10%3)#reszta z dzielenia
print(10**3)#do potegi

import math
print(round(2.9)) #zaokraglic
print(abs(-2.9)) #wartosc bezwzgledna

print(math.ceil(2.2))

#kiedy podajemy cos (input) komputer traktuje to jako string
#x = input("x: ")
#y = int(x) + 1
#print(y)

#BOOL
#nie jest 0 -> true


# != -> nie rowna sie
# >>> "bag" > "apple" bo asci b wiekszy niz a
# >>> "BAG" != "bag" bo wieksze literymaka wieksze asci
print(ord("b"))
print(ord("B"))


#PETLA IF

t=120
if t==122:
    print("ghfhjfyht")
elif t==121:
    print("abcdef")
else: print("cosinnego")

if zmienna:
    print("true")
else: print("false")


#ZADANIE
#wiek = input("Wiek= ")
#if int(wiek) >= 18:
#    print("Ilegible")
#else: print("Not ilegible")


#PETLA RANGE(FOR)
for z in range(4):
    print(z)
for a in range(4,10):
    print(a)


















