import math #jednak trzeba dodawać niektóre biblioteki TwT

t = " pies je kOta"
print(t.upper()) # przekształca litery na wielkie
print(t.lower())
print(t.title())
print(t.lstrip())
print(t.lower())
print(t.find("O"))
print(t.replace("O", "p"))
print("si" in t) # czy dany ciąg znaków występuje w danyej zmiennej?
print("si" not in t)
print(10/3)
print(10//3) # zaokrągla wynik dzielenia
print(10%3) # reszra z dzielenia
print(10 ** 3) # potęgi

x = 10

x = x + 3
print(x)

x += 3
print(x)

# do matha

print(round(2.9)) # zaokrąglij
print(abs(-2.9)) # wartość bezwzględna
print(math.ceil(2.2)) # zaokr. do góry
print(math.floor(2.8)) # zaokrągla do dołu

x = input("x: ")
y = int(x) + 1
print(y)

z = 0
a = 5
m = ""

print(bool(m))
print(bool(z))
print(bool(a)) # / jakakolwiek inna liczba
print(10 != 10) # różne

print(ord("b"))
print(ord("B"))
print("bag" > "apple") # kod ASCII; porownuje pierwsze litery

a = input("podaj a: ")

if int(a) == 20:
    print("a jest równe 20")
elif int(a) < 20:
    print("a jest mniejsze od 20")
else:
    print("a jest większe od 20")

if x:
    print("k")
else:
    print("None")

age = input("podaj wiek: ")
if int(age) >= 18: # lub wcześniej: int(input("podaj wiek: "))
    print("Eligible")
else:
    print("Not eligible")