# L = [3, 7, 6, 1, 3, 3, 5, 4]

# print(L)

# print(L[1])

# print(L[6])

# print(len(L))

# # print("\n") - printuje pustą linijkę

# for elem in L:
#   print(elem, end=" ")
# print("\n")

# for i in range(len(L)):
#   print(L[i], end=" ")
# print("\n") 






# //Wygeneruj tablicę n losowych liczb:
# from random import randint
# L = [for i in range(20): randint(1,21)]



# 1. Znajdź największą liczbę w tablicy
# 2. Znajdź najmniejszą liczbę w tablicy
# 3. Podaj ile razy występuje najwieksza liczba w tablicy
# 4. Podaj ile razy występuje najmniejsza liczba w tablicy
# 5. Podaj rozpiętość tablicy (różnica max - min)
# 6. Podaj sumę liczb w tablicy
# 7. Podaj średnią wartość liczb w tablicy
# 8. Których liczb jest więcej w tablicy: parzystych czy nieparzystych?
# 9. Ile w tablicy jest liczb pierwszych?
# 10. Podaj v-ce max i v-ce min liczb tablicy



from random import randint
L = [randint(1,21) for i in range(20)]
print(max(L))
print(min(L))
print(L.count(max(L))