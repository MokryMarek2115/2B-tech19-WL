# Zad 1
# a=int(input())
# b=int(input())
# c=int(input())

# if b - a == c - b:
#   print("Ciąg arytmetyczny")
# elif b / a == c / b:
#   print("Ciąg geometryczny")
# elif a > b > c:
#   print("Ciąg malejący")
# elif a < b < c:
#   print("Ciąg rosnący")


# Zad 2
# s = 0
# for i in range(100,1000):
#   if i % 8 == 0 and i % 16 != 0:
#     s = s + i
# print(s)

# Zad 3
# for i in range(99,9,-1):
#   if i % 7==0:
#     wielok = i
#     break

# ilosc=0
# for i in range(1000,10000):
#   if i % wielok==0:
#     ilosc=ilosc + 1

# print(ilosc)



# Zad 4
# ilosc=0
# for i in range(10,100):
#   cd = i // 10
#   cj = i % 10
#   if cd >= 2*cj:
#     ilosc += 1
# print(ilosc)


# Zad 5
ilosc=0
s=0

for i in range(10,100):
  cs = i // 100
  cd = (i % 100) // 10
  #cd = (i // 10) % 10
  cj = i % 10
  if cd >= 2*cj:
    ilosc += 1
print(ilosc)
