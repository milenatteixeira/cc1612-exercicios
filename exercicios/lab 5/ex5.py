from random import randint
A = []

for linha in range(10):
    a = []
    for coluna in range(5):
        a.append(randint(0,99))
    A.append(a)
print('MATRIZ A')
for linha in range(len(A)):
  for coluna in range(len(A[linha])):
    print("%2d" % A[linha][coluna], end=" ")
  print()

  
print()
print('MATRIZ A TRANSPOSTA')
for coluna in range(len(A[coluna])):
  for linha in range(len(A)):
    print("%2d" % A[linha][coluna], end=" ")
  print()
