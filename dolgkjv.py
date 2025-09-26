nevek = ["Tibi", "Evi", "Sanyi", "Karcsi"]
nemek = [1,2,1,1]
# hany fiu van?
# Fiuk nevei:
# Hany % a fiuk aranya


for i in range(len(nevek)):
     print(nevek[i])

fiunevek = []
for i in range(len(nevek)):
     if nemek[i] == 1:
          fiunevek.append(nevek[i])

print(fiunevek)
print(f"(len(fiunevek))fiú van.")

print(f"(len(fiunevek)/len(nevek))")


