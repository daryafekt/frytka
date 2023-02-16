zmienna = "ciąg znaków"
print(len(zmienna))  #drukuje na ekranie ilosc znakow(ze spacjami!!!!)
print(zmienna[0])# bedzie "c", poniewaz pierwszy znak jest 0(mozna potraktowac string jak tablice)
print(zmienna[0:5])#od drugiego do 6 znaku
print(zmienna[-5]) # 5 od konca
print(zmienna[3:]) #od 4 znaku i do konca
print(zmienna[:5]) # od poczatku do 6 znaku
print(zmienna[:]) #maksymalna skrajnie z jednej i z drugiej strony
print(zmienna[::2]) # co drugi znak(wszystko od poczatku do konca)

#[x:y:z]
# x-pocztek y-koniec z-krok
print(zmienna) #caly string

imie = "Darya"
nazwisko = "Feaktsistava"
print(imie + " " + nazwisko)
print(imie, nazwisko, end=".") #skopiowac linie - Ctl+D !!!!!!!!!!!!!!!!!!!!!!!!!!!!
print(imie * 3, nazwisko, end=".") #end nie przenosi do nastepnej linii
print(imie * 3, nazwisko, end="\n") #\n konczy linie
print(imie * 3, nazwisko, end=".")

#FORMATOWANY STRING
print("Witaj," , imie, "bjjdjdjdhdj")
print(f"Witaj,{imie}bjjdjdjdhdj") #f na poczatku zeby dac programowi znac, ze to formatowany string

print(type(imie)) #drukuje typ zmiennej!!


x=input("podaj swoj wiek: ")#zaznaczyc wszystko i wpisac 1 cudzyslow  => wszystko w cudzyslowie
print(int(x) + 2) #zmienic typ zmiennej

#fill() - wypelnic; .zfill() - wypelnic zerami
james_bond=7
print(str(james_bond).zfill(3))


