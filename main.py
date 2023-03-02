imie = "jan"

print(bool("")) #zwraca false
print(bool("tomek")) #zwraca true

if imie: #imie jest truthy
    print("imie istnieje")

successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break #wyjście z pętli

successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")

for x in range(5): #x do pieciu czyli od 0 do 4
    for y in range(3): #y od 0 do 2
        print(f"({x}, {y})") #wydrukowac wspolrzedne

#iterable
for x in ("Phyton"):
    print(x)

#number = 100
#while number > 0:
   # print(x//2) #coś tutaj jeszcze
count=0
for x in range(1,10):
    if x %2 == 0:
        count += 0
        print(x // 2) == 0

def nazwafunkcji():
    print("Hi there")
    print("Welcome abroad")
nazwafunkcji()

def dodawanie(x,y): #ilość zmiennych musi byc rowna ilosci tego tam 2 i 3 czyli ich jest dwa tak jak dwa sa x i y ##aby wiecej dodaj w def =0
    print(x + y)
dodawanie(2,3)
