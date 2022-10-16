# # Zad 1
# n = int(input())
# if n % 3 == 0:
#   print ("Tak")
# else:
#   print ("Nie")

# Zad 2 
# n = int(input())
# if n >= 100 and n <1000 and n % 17 == 0:
#   print("Tak")
# else:
#   print("Nie")

# Zad 3
# wiek = int(input())
# if wiek >= 18:
#   print("Tak")
# else:
#   print("Nie")

# Zad 4
# LIMIT = 20
# waga = int(input())
# if waga <= LIMIT:
#   print("Jedz ze spokojem")
# else:
#   print("Lepiej nie jedz")

# Zad 5
# a = int(input())
# b = int(input())
# c = int(input())
# if (c>a and c<b) or (c>b and c<a):
#   print("Tak")
# else:
#   print("Nie")

# Zad 6
# a = int(input())
# p = int(input())
# if (a**p-a) % p == 0:
#   print("Tak, spełnia MTF")
# else:
#   print("Nie, nie spełnia")

# Zad 7
# p = int(input())
# k = int(input())
# s = int(input())
# if (s*3>=k):
#   print("tak")
# else:
#   print("nie")



# 1a
# a = int(input())
# b = int(input())
# if (a+b) % 2 == 0:
#   print("Tak")
# else:
#   print("Nie")

# 2a
# a = int(input())
# g = int(input())
# if (a+g)/2 > (a*g)**(1/2):
#   print("Tak")
# else:
#   print("Nie")

# 3a
# k = int(input())
# l = int(input())
# m = int(input())
# if k==l:
#   print("tak równe są k i l")
# if k==m:
#   print("tak równe są k i m")
# if l==m:
#   print("tak równe są l i m")
# else:
#   print("Nie")

# Zad 4a
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())



# Zad 5a
# a = int(input())
# b = int(input())
# c = int(input())
# if (a+b)>c and (a+c)>b and (b+c)>a:
#   print("Tak")
# else:
#   print("Nie")

# Zad 6a
a = int(input())
b = int(input())
c = int(input())
if (a+b)>c and (a+c)>b and (b+c)>a and (c**2) == (a**2+b**2):
  print("Tak, trójkąt prostokątny")
if (a+b)>c and (a+c)>b and (b+c)>a and (c**2) > (a**2+b**2):
  print("Tak, trójkąt rozwartokątny")
if (a+b)>c and (a+c)>b and (b+c)>a and (c**2) < (a**2+b**2):
  print("Tak, trójkąt ostrokątny")

