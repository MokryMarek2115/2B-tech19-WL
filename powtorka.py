# print(11/4)
# print(11//4) dzielenie całkowite


# jak wydobyc ostatnie 2 cyfry z liczby albo cyfre setek
# n=12345
# print((n%1000)//100)


# pierwiastek 
# from math import sqrt
# print(sqrt(576))
# print(576**(1/2))
# print(8**(1/3))


# == >= <= > < != - operatory porownan
# petla z liczbami 3 cyfrowymi podzielnymi przez 13 i niepodzielnymi przez 4

# for i in range(100,1000):
#   if i % 13 == 0 and i % 4 > 0:
#     print(i)


# łączenie warunkow 
# a, b, c = 3, 5, 7
# # if a < b < c:
# if a < b and b < c:


# for i in range(100, 1000, 15):
#   print(i)


# n = 24
# for i in range(1,25):
#   if n % i == 0:
#     print(i)


# n=24
# suma=0
# ilosc=0
# for i in range(1, 25):
#   if n % i == 0:
#     print(i)
#     suma = suma + i
#     ilosc = ilosc + 1
# print("suma", suma)
# print("ilosc", ilosc)


# we:4
# wy:406 (100+101+102+103)
# k=4
# suma=0
# ilosc=0
# for i in range(100, 1000):
#   suma = suma + i
#   ilosc = ilosc + 1
#   if ilosc == k:
#     break
# print(suma)

# break-wyjscie z petli


# k=4
# suma=0
# for i in range(100, 100 + k):
#   suma = suma + i
# print(suma)


# n=int(input())
# a = 0
# b = 1
# suma = 0
# for i in range(n):
#   a, b = b, a + b
#   suma = suma + b
# print(suma)


# n=496
# suma = 0
# for i in range(1, n):
#   if n % i == 0:
#     suma = suma + i

# if suma == n:
#   print("tak")
# else:
#   print("nie")