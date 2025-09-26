teljes_nev = input("Kérlek, adj meg egy nevet: ")

magyar_betuk = "aábcdeéfghiíjklmnoóöőpqrstuúüűvwxyz"
monogram = ""
i = 0

while i < len(teljes_nev):
    # Ha betűt találunk, ez szó kezdete
    if teljes_nev[i].lower() in magyar_betuk:
        szo_betuk = ""
        # gyűjtsük a szó betűit
        while i < len(teljes_nev) and teljes_nev[i].lower() in magyar_betuk:
            szo_betuk += teljes_nev[i].upper()
            i += 1
        # szó feldolgozása
        if len(szo_betuk) == 1:
            monogram += szo_betuk  # 1 betűs szó → 1 betű
        else:
            monogram += szo_betuk[:2]  # 2 vagy több betű → első 2 betű
    else:
        i += 1  # nem betű átugrása

print(monogram)