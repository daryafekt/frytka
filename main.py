M=1000
X=10
V=5
C=100
I=1
D=500
L=50

zmienna=input("podaj datę ")
a=0
for i in range(0, len(zmienna)):
    if zmienna[i]=="M": a=a+M
    if zmienna[i]=="X": a=a+X
    if zmienna[i-1]=="I": a=a-I
    if zmienna[i]=="V": a=a+V
    if zmienna[i]=="C": a=a+C
    if zmienna[i]=="D": a=a+D
    if zmienna[i]=="L": a=a+L
print(a)
