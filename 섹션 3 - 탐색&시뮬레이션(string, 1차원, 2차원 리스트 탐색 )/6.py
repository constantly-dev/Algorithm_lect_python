n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

max_val = -2147000000

# 행의 합 
for i in range(n):
  sum_val = 0
  for j in range(n):
    sum_val += a[i][j]
  
  if sum_val > max_val:
    max_val = sum_val

# 열의 합 
for i in range(n):
  sum_val = 0
  for j in range(n):
    sum_val += a[j][i]
  
  if sum_val > max_val:
    max_val = sum_val

# 대각선의 합
sum_val = 0

for i in range(n):
  sum_val += a[i][i]

if sum_val > max_val:
  max_val = sum_val


sum_val = 0

for i in range(n):
  sum_val += a[i][n-i-1]

if sum_val > max_val:
  max_val = sum_val


print(max_val)


# 강의 풀이 -----------
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

largest = -2147000000
for i in range(n):
  sum_row = sum_col = 0
  for j in range(n):
    sum_row += a[i][j]
    sum_col += a[j][i]
  
  if sum_row > largest:
    largest = sum_row
  if sum_col > largest:
    largest = sum_col
  

sum_row = sum_col = 0
for i in range(n):
  sum_row += a[i][i]
  sum_col += a[n-i-1][n-i-1]

if sum_row > largest:
  largest = sum_row
if sum_col > largest:
  largest = sum_col

print(largest)