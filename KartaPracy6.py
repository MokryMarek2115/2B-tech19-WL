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

# Zad 4
ilosc=0
for i in range(10,100):
  cd = i // 10
  cj = i % 10
  if cd >= 2*cj:
    ilosc += 1
print(ilosc)