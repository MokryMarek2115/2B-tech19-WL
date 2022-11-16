# Zad 1 Sprawdzanie czy liczba jest pierwsza
#liczba pierwsza to taka liczba ktora sie dzieli tylko przez 1 i sama siebie, np. 2,3,5,7,11,13,17,19,23.....
#dzielniki własciwe - dzielniki liczby poza 1 i nia sama

n=int(input())
for i in range(2, n):
  if n % i == 0:
    print("Liczba nie jest pierwsza")
    exit(0)
print("Liczba jest pierwsza")