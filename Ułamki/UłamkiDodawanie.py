# a=int(input())
# b=int(input())
# c=int(input())
# d=int(input())

# x, y=b, d
# ilocz=x*y

# while  y > 0:
#   x, y =y, x%y
# NWW = ilocz//x

# e = (NWW // b)*a
# f = (NWW // d)*c
# g = e + f

# print(f"{a}/{b} + {c}/{d} = {e}/{NWW} + {f}/{NWW} = {g}/{NWW}")

# NWW mianownikow
# iloczyn mianownikow / (NWD)mianownikow





p=int(input("Podaj ile (od początku) liczb pierwszych chcesz"))

i = 2
licznik = 0

while 1:
  flaga = True;
  for j in range(2, int(i**0.5)+1):
    if i % j == 0:
      flaga = False
      break
  if flaga == True:
    print(i, end=" ")
    licznik += 1
  if licznik == p:
    break
  else:
    i = i + 1