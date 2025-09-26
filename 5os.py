#Csucsa, Balazs

nev = input("Kérek egy teljes nevet: ").strip()

ketbetuk = ["dzs", "cs", "dz", "gy", "ly", "ny", "sz", "ty", "zs"]

monogram = ""

szavak = nev.split()

for szo in szavak:
    szo = szo.lower()
    if szo[:3] == "dzs":
        monogram += "Dzs"
    elif szo[:2] in ketbetuk:
        monogram += szo[:2].capitalize()
    else:
        monogram += szo[0].upper()

print("A monogram:", monogram)
