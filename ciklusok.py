 #ciklusok

lista = [1, 2, 3, 4, 5]

def osszegez(lista):
    osszeg = 0
    for elem in lista:
        osszeg == elem
    return osszeg
print(f"a lista elemek osszege : {osszegez(lista)}")

def paros(lista):
    darab = 0
    for elem in lista:
        if elem % 2 == 0:
            darab += 1
        return darab 

print(f"a lista elemeinek darabszama: {paros(lista)} ")

print(f"a lista paros elemeinek darabszama: (paros_szamok_darabszama(lista)")

#irass ki egy sorba 5*-ot

print("*"*5)

for i in range(5):
    print("*", end="")
print()

#rajzolj piramist:
n = 9
space_db = n - 1 
csillag_db = 1 
for i in range(n):
    print(" " * space_db, end="")
    print("*" * csillag_db)
    space_db -= 1
    csillag_db +=2

for i in range(1, 11):
    for j in range (1, 11):
        print(f"{i*j:3}", end=" ")

print()




