# Zad 1 Sprawdzanie czy liczba jest pierwsza
#liczba pierwsza to taka liczba ktora sie dzieli tylko przez 1 i sama siebie, np. 2,3,5,7,11,13,17,19,23.....
#dzielniki własciwe - dzielniki liczby poza 1 i nia sama

# n=int(input())
# for i in range(2, n):
#   if n % i == 0:
#     print("Liczba nie jest pierwsza")
#     exit(0)
# print("Liczba jest pierwsza")


# 2. Generowanie liczb pierwszych(w przedziale [p, q])

# p=int(input("Podaj do ilu mam szukac liczb pierwszych"))
# q=int(input("Podaj do ilu mam szukac liczb pierwszych"))

# for i in range(p, q+1):
#   flaga = True;
#   for j in range(2, i):
#     if i % j == 0:
#       flaga = False
#       break
#   if flaga == True:
    # print(i, end=" ")

# 3. Generowanie liczb pierwszych(pierwsze n liczb pierwszych)

# p=int(input("Podaj ile (od początku) liczb pierwszych chcesz"))

# i = 2
# licznik = 0

# while 1:
#   flaga = True;
#   for j in range(2, int(i**0.5)+1):
#     if i % j == 0:
#       flaga = False
#       break
#   if flaga == True:
#     print(i, end=" ")
#     licznik += 1
#   if licznik == p:
#     break
#   else:
#     i = i + 1

#
#
#
#
#
#
# NWW 2 odejmowanie
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


# NWW 2 modulo
a=int(input())
b=int(input())

iloczyn = a * b

while b > 0:
  a, b =b, a%b
print(a)

