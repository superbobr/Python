n = int(input())
m = int(input())
matrix = []

for _ in range(n):
    matrix.append([int(i) for i in input().split()])

largest = matrix[0][0]
largest_index = [0, 0]

for i in range(n):
  for j in range(m):
    if matrix[i][j] > largest:
      largest = matrix[i][j]
      largest_index = [i, j]
      
print(*largest_index)
