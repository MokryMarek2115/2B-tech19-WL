# Fynkcja ord() - zwraca kod ASCII znaku
# print(ord("A"))
# print(ord("Z"))
# # w python kod ASCII wielkich liter A - Z od 65 do 90

# # Funkcja chr() - zwraca znak dla danego kodu
# print(chr(66))
# print(chr(77))

# Zadanie testowe: wypisz alfabet wielkich liter
# for i in range(65, 91):
#   print(chr(i), end=" ")


# string w python - "lista"

# napis = "ARGENTYNA"
# print(napis[0], napis[1], napis[2])


# for i in range(len(napis)):
#   print(napis[i])


# Cezar

napis = input()
szyfr = " "
# print(napis[0], napis[1], napis[2])
# print(len(napis))

for i in range(len(napis)):
  print(napis[i])
  szyfr = szyfr + chr(65 +(ord(napis[i])-65+3) % 26)
print(szyfr)