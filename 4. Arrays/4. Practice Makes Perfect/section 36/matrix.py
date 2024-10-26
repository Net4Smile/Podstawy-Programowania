def identity_matrix(n):
  matrix = []
  for i in range(n):
    matrix.append([])
    for j in range(n):
      if i == j:
        matrix[i].append(1)
        continue
      matrix[i].append(0)
  return matrix

for i in range(len(identity_matrix(3))):
  print(" ".join(map(str, identity_matrix(3)[i])))

print("\n")
 
for i in range(len(identity_matrix(5))):
  print(" ".join(map(str, identity_matrix(5)[i])))

print("\n")

for i in range(len(identity_matrix(8))):
  print(" ".join(map(str, identity_matrix(8)[i])))