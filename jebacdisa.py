# WSTĘP


# ZAD 1 - podaje sume liczb 3-cyfrowych
# s = 0
# for i in range(100,1000):
#   s += i
# print(s)


# ZAD 2 - podaje sume dwucyfrowych wielokrotnosci cyfry 6 i ich ilosc
# s = 0
# ilosc = 0
# for i in range(6, 96, 6):
#   s += i
#   ilosc += 1
# print(s, ilosc)


# ZAD 3 - podaje najwieksza liczbe z 4 losowo wygenerowanych
# from random import randint
# L = [randint(1000, 10000) for i in range(4)]
# print(L)
# print(max(L))


# ZAD 4 - suma cyfr w liczbie
# def oblicz_sume_cyfr(liczba):
#     suma = 0
#     for cyfra in str(liczba):                                          
#         suma += int(cyfra)
#     return suma

# liczba = input("Podaj liczbę: ")
# suma_cyfr = oblicz_sume_cyfr(liczba)
# print("Suma cyfr w liczbie", liczba, "to:", suma_cyfr)
 




# liczba = int(input("Podaj liczbę: "))

# suma_cyfr = 0
# while liczba != 0:
#     cyfra = liczba % 10
#     suma_cyfr += cyfra
#     liczba //= 10

# print("Suma cyfr w liczbie", liczba, "to:", suma_cyfr)


# liczba = input("Podaj liczbę: ")
# suma = 0

# for cyfra in liczba:
#     suma += int(cyfra)

# print("Suma cyfr w liczbie", liczba, "to:", suma)



# ZAD 5 - najmniejsza cyfra w liczbie
# liczba = int(input("Podaj liczbę trzycyfrową: "))

# cyfra_setki = liczba // 100
# cyfra_dziesiatek = (liczba // 10) % 10
# cyfra_jednosci = liczba % 10

# najmniejsza_cyfra = min(cyfra_setki, cyfra_dziesiatek, cyfra_jednosci)

# print("Najmniejsza cyfra w liczbie", liczba, "to:", najmniejsza_cyfra)



# ALGORYTMY:


# ZAD 1 - liczby pierwsze
# n=int(input())
# for i in range(2, n):
#   if n % i == 0:
#     print("Liczba nie jest pierwsza")
#     exit(0)
# print("Liczba jest pierwsza")



# ZAD 2 - liczby zlozone
# n=int(input())
# for i in range(2, n):
#   if n % i == 0:
#     print("Liczba jest zlozona")
#     exit(0)
# print("Liczba nie jest zlozona")


# ZAD 3 - liczby względnie pierwsze z 24
# a=int(input())
# b=24
# from math import gcd
# if gcd(a,b)==1:
#   print("Liczba jest względnie pierwsza z 24")
# else:
#   print("Liczba nie jest względnie pierwsza z 24")


# ZAD 4
# napis = input("Podaj coś do zaszyfrowania: ")
# szyfr = ""
# print(napis[0], napis[1], napis[2])
# print(len(napis))

# for i in range(len(napis)):
#     szyfr = szyfr + chr(65 + ((ord(napis[i])-65+3) % 26))
# print(szyfr)





# napis = input("Podaj napis do szyfracji: ")
# szyfr = ""
# klucz = int(input("Podaj klucz: "))

# for i in range(len(napis)):
#     szyfr = szyfr + chr(65 + (ord(napis[i]) - 65 + klucz) % 26)
# print("Szyfracja:", szyfr)
    


# ZAD 5 
# from math import gcd
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

# x, y = b, d
# ilocz = x * y

# while y > 0:
#     x, y = y, x % y
# NWW = ilocz // x

# e = (NWW // b) * a
# f = (NWW // d) * c
# g = e + f

# liczba_mieszana = g // NWW  # Liczba całkowita
# ul_wlasc = abs(g % NWW)  # Ułamek właściwy
# gcd_wart = gcd(ul_wlasc, NWW)  # Największy wspólny dzielnik

# if ul_wlasc == 0:
#     print(f"{a}/{b} + {c}/{d} = {liczba_mieszana}")
# else:
#     if liczba_mieszana == 0:
#         print(f"{a}/{b} + {c}/{d} = {ul_wlasc}/{NWW}")
#     else:
#         print(f"{a}/{b} + {c}/{d} = {liczba_mieszana} {ul_wlasc // gcd_wart}/{NWW // gcd_wart}")



# ZAD 6 - NWW
# a=int(input())
# b=int(input())
# iloczyn=a*b

# while a!=b:
#   if a>b:
#     a=a-b
#   elif b>a:
#     b=b-a
# NWD=a
# print(iloczyn//NWD)




# a=int(input())
# b=int(input())

# iloczyn = a * b

# while b > 0:
#   a, b =b, a%b
# print(a)




# NAPISY


# ZAD 1 - liczy ile jest c w wyrazie
# a = input()
# print(a.count("c"))



# ZAD 2
# napis = input("Wprowadź napis: ")

# nierosnacy = True

# for i in range(len(napis) - 1):
#     if napis[i] < napis[i+1]:
#         nierosnacy = False
#         break

# if nierosnacy:
#     print("Litery w napisie występują w porządku nierosnącym.")
# else:
#     print("Litery w napisie nie występują w porządku nierosnącym.")


# ZAD 3
# a = input("Wprowadź pierwszy wyraz: ")
# b = input("Wprowadź drugi wyraz: ")
# c = input("Wprowadź trzeci wyraz: ")

# if len(a) > len(b) and len(a) > len(c):
#     print("najdluzszy a")
# elif len(b) > len(a) and len(b) > len(c):
#     print("najdluzszy b")
# elif len(c) > len(a) and len(c) > len(b):
#     print("najdluzszy c")



