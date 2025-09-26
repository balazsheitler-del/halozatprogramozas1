gyumolcsok = ["eper", "dinnye", ]

jegyek = [2, 5]
jegyek.append(1)
gyumolcsok.append("alma")
print(jegyek)
print(gyumolcsok)
jegyek.sort()
print(jegyek)
# print(sorted(jegyek))
gyumolcsok.remove ("dinnye")
print(gyumolcsok)
gyumolcsok.insert(1, "banan")
print(gyumolcsok)
# gyumolcsok = []
jegyek.reverse()
print(jegyek)
print(gyumolcsok.index("banan"))
print(jegyek.count(5))
print(sum(jegyek))
print(min(jegyek))
print(max(jegyek))
print(len(jegyek))

#string -eket tartalmazo lista kiirasa

print(f"{','.join.gyumolcsok}")

#int-eket tartalmazo lista kiirasa

print(f"{','.join.map(str, jegyek)}")






