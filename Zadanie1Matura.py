a=int(input())
b=int(input())

S1=0
S2=0

for i in range(1, a):
  if a % i==0:
    S1 =+ i
print(S1)
for p in range(1, b):
  if b % p == 0:
    S2 += p
print(S2)

if S1 == b+1 and S2 == a+1:
  print("TAK")
else:
  print("NIE")
