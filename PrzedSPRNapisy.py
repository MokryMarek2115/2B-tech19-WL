# 1. Wczytaj dowolny napis i wypisz z niego pierwszą i ostatnią literkę

# x = input()
# print(x[0], x[-1])
# print(x[0], x[len(x)-1])

# 2. Wczytaj dowolny napis i wypisz z niego literki bez pierwszej i ostatniej

# a = input()
# for i in range(1, len(a)-1):
#     print(a[i], end="")
# print()

# print(a[1:len(a)-1])

# 3. Wypisz 4 ostatnie literki z wpisanego napisy w kolejności od końca

# b = input()

# for i in range(len(b)-1, len(b)-5, -1):
#     print(b[i], end="")
# print()

# print(b[len(b)-1:len(b)-5:-1])

# L = list(b)
# L.reverse()
# b = "".join(L)
# for i in range(4):
#     print(b[i], end="")
# print()

# 4. Waga napisu to suma kodów ascii jego liter. Zważ wpisny napis

# c = input()
# suma = 0
# for i in c:
#     suma += ord(i)
# print(suma)

# 5. Policz ile we wpisanym napisie jest liter A.

# e=input()
# ilosc = 0
# for x in e:
#   if x == "A":
#     ilosc = ilosc + 1
# print(ilosc)

# print(e.count("A"))

# 6. Podaj dominującą literkę we wpisanym napisie. Niech to będzie tylko jedna literka.

# g = input()
# maks=0
# for x in  g:
#   if g.count(x) > maks:
#     maks = g.count(x)
#     literka = x
# print(literka, maks)
  
# 8. Sprawdź czyh w napisie występują trzy podciągi "LA"

h = input()
ilosc=0
for i in range(len(h)-1):
    if h[i : i+2] == "LA":
      ilosc += 1
if ilosc == 3:
  print("TAK")
else:
  print("NIE")


# print(h.count("LA"))





# 1. Wczytaj dowolny napis i wypisz z niego pierwszą i ostatnią literkę
# x = input()
# print(x[0], x[-1])
# print(x[0], x[len(x)-1])
# 2. Wczytaj dowolny napis i wypisz z niego literki bez pierwszej i ostatniej
# a = input()
# for i in range(1, len(a)-1):
#     print(a[i], end="")
# print()
# print(a[1:len(a)-1])
# 3. Wypisz 4 ostatnie literki z wpisanego napisy w kolejności od końca
# b = input()
# for i in range(len(b)-1, len(b)-5, -1):
#     print(b[i], end="")
# print()
# print(b[len(b)-1:len(b)-5:-1])
# L = list(b)
# L.reverse()
# b = "".join(L)
# for i in range(4):
#     print(b[i], end="")
# print()
# 4. Waga napisu to suma kodów ascii jego liter. Zważ wpisny napis
# c = input()
# suma = 0
# for i in c:
#     suma += ord(i)
# print(suma)
# 5. Policz ile we wpisanym napisie jest liter A.
# 6. Podaj dominującą literkę we wpisanym napisie. Niech to będzie tylko jedna literka.
# ZAGADNIENIA Napisy 
# - len, for, "foreach", ord, chr
# - indeksy, zakresy
# - konwersje list <-> napis
# - list - sort reverse
# - split, join
# Algorytmy - anagram, palindom, Boyer-Moore
# Wszystkie zadania wykonujemy na 26-znakowym
# alfabecie maturalnym: od A (65) do Z (90)
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# Przykładowe zadania:
# 1. Wczytaj dowolny napis i wypisz z niego pierwszą i ostatnią literkę
# a = input()
# print(a[0], a[-1])
# print(a[0], a[len(a)-1])
# 2. Wczytaj dowolny napis i wypisz z niego literki bez pierwszej i ostatniej
# b = input()
# for i in range(1, len(b)-1):
#     print(b[i], end="")
# print()
# print(b[1:len(b)-1])
# print(b[1:-1])
# L = list(b)
# L.pop(0)
# L.pop(-1)
# b = "".join(L)
# print(b)
# 3. Wypisz 4 ostatnie literki z wpisanego napisy w kolejności od końca
# c = input()
# print(c[-1:-5:-1])
# for i in range(len(c)-1,len(c)-5,-1):
#     print(c[i], end="")
# print()
# L = list(c)
# L.reverse()
# c = "".join(L)
# print(c[:4])
# 4. Waga napisu to suma kodów ascii jego liter. Zważ wpisny napis
# d = input()
# s = 0
# for x in d:
#     s += ord(x)
# znak = s // len(d)
# print(chr(znak))

# 5. Policz ile we wpisanym napisie jest liter A.


# e = input()
# ilosc = 0
# for x in e:
#     if x == "A":
#         ilosc += 1
# print(ilosc)

# 6. Podaj dominującą literkę we wpisanym napisie. 
# Niech to będzie tylko jedna literka.

# g = input()
# maksik = 0
# for x in g:
#     if g.count(x) > maksik:
#         maksik = g.count(x)
#         literka = x
# print(literka, maksik)


# 7. Znajdź literkę-dominantę w napisie (może ich być kilka, a może nie być żadnej)

# 8. Sprawdź czy w napisie występują trzy podciągi "LA"



h = input()
ilosc = 0
for i in range(len(h)-1):
    if h[i:i+2] == "LA":
        ilosc += 1
if ilosc == 3:
    print("TAK")
else:
    print("NIE")

# 9. Znajdź "średnią literkę" w napisie. (Przejdź na kody ASCII i jeśli wynik będzie
# ułamkowy to zaokrąglij średnią w dół)
# 10. Wypisz literki, których nie ma w napisie
# 11. Znajdź ilość trzyznakowych palindromów w napisie (trzy literki koło siebie)
