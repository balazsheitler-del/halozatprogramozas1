print("Szia", end=" ")
print("Tibi")
print("Szia", "Tóth", "Karcsi", "!", sep="")
print("Szia Tóth Karcsi!")
nev = "Tóth Karcsi"
print(f"Szia {nev}!")
print("Szia", "Peti", sep="\n", end="!") #\t
#adattípusok
# int()
# float()
# str()
# bool()
# list()
# set()
# tuple()
print()
print(int("5"))
print(float(5))
print(type(str(5.0)))
print(bool(-1))
print(["hétfő", "kedd", "szerda"])
napok = ["hétfő", "kedd", "szerda"]
print(f"Napok: {napok}")
nevek = ["Tibi", "Sanyi", "Tibi"]
print(f"Nevek: {set(nevek)}")
print(tuple([1,2,3]))


# HF: git parancsok:
# git init : adott mappa verziókövetésének indítása
# git add . :
# git config --global user.name "A Te GitHub felhasználóneved"
# git config --global user.email "a_te_email_cimed@example.com"
# git remote add origin https://github.com/FELHASZNÁLÓNÉV/myproject.git
# git branch -M main
# git push -u origin main
# git clone https://github.com/FELHASZNÁLÓNÉV/myproject.git
