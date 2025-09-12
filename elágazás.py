import random

gondolt_szam = random.randint(1,3)

#print(f"a gondolt szam : (gondolt_szam)")
bekert_szam = int(input ("kérem a tippet: "))

if gondolt_szam == bekert_szam: 
    print("kitaláltad!")
else: 
    if gondolt_szam > bekert_szam: 
        print("nagyobbra gondoltam4")
    elif gondolt_szam > bekert_szam:
        print("nagyobbra fondoltam!")
    else:
        print("kisebbre gondoltam!")


# készíts függvényt előjel néven, mely átvesz egy egész számotés az előjelét adja vissza


def elojel(szam):
    if szam >= 0:
        return "+"
    else:
        return "-"

szam = int(input ("kérek egy számot előjellel: "))

print(f"a {szam} elojele: ({elojel (szam)}).")

print(f"A {szam} elojele: {'+'if szam>=0 else '-'}.")

def tesztesetek():
    teszt(5, "+");
    teszt(-3, "-")
    teszt(0, "+")
    teszt(1, "-")
    #...

def teszt(szam, elvart_elojel):
    if elojel (szam) == elvart_elojel:
        print(f"elojel({szam}) == {elvart_elojel} true")
    else:
        print(f"elojel({szam}) == {elvart_elojel} false")

tesztesetek()