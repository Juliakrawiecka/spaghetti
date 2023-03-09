#zmienna data typu str 17-02-2023
b="09-03-2023"
#b=input("Podaj date w formacie dd-mm-rrrr")
d= b[:2]
m= b[2:6]
r= b[-4:]
ndata= r+m+d
print(ndata)

ld=b.split("-")
print(ld)
print(type(ld)) #lista
lnd=ld[::-1]
print(lnd) #lista od tyłu
print("-".join(lnd)) #elementy z listy. join laczy i zamienia w stringa