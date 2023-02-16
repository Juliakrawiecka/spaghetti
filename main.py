# notatki github
course = "PYTHON PROGRAMMING"
print(len(course))  #liczba znaków ze spacjami
print(course[0]) #liczba znaków o indeksie 0 (pierwsza litera) 1 (druga litera)
print(course[5:2]) #przedział
print(course[-1]) #od końca
print(course[2:]) #od 2 do końca
print(course[:3]) #do 3 znaków (nie włącznie)
print(course[:]) #maksymalna skrajnosć z jednej i drugiej (tak samo jak bez niczego)
print(course[::2]) #wszystko od początku do końca ale co drugi element

# [x:y:z]
# x - początek
# y - koniec
# z - krok

a = "Julia"
b = "krawiecka"
print (a+ " " +b)
print(a * 3, b, end="---") #ctrl +d - kopiowanie
print(a * 3, b, end="---") #ctrl +d
#ctrl z - cofanie
print(f"witaj {a} cześć") #f ważne do zmiany i podstawienia
print(type(a)) #zwraca jakiego typu jest dana zmienna

x = input('Podaj swój wiek: ')
print(int(x)+2)

james_bond = 7
# nasz cel to 007
# zfill() - dodaj zero
print(str(james_bond).zfill(3)) #do trzeciego znaku wypełnij zerem
