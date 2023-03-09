dd=input("podaj dzień= ")
mm=input("podaj miesiąc= ")
rr=input("podaj rok= ")

data=dd+"-"+mm+"-"+rr

data2=rr+"-"+dd+"-"+mm
print(data2)


b=input("podaj datę w formacie dd-mm-rr ")
nowa_data=b.split("-") #lista, podzieli string na wyrazy, oddzielone "-"
print(nowa_data)
NOWA_DATA=nowa_data[::-1]
print(NOWA_DATA)
print("-".join(NOWA_DATA))