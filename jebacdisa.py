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
# if a // 2 > 0 and a // 3 > 0 and a // 4 > 0 and a // 6 > 0 and a // 8 > 0 and a // 24 > 0:
#   print("Liczba nie jest względnie pierwsza z 24")
# else:
#   print("Liczba jest względnie pierwsza z 24")




# NAPISY


# ZAD 1 - liczy ile jest c w wyrazie
# a = input()
# print(a.count("c"))


# ZAD 2
