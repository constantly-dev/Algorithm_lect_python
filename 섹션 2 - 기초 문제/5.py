# 완벽히 스스로 풀이 X

n, m = map(int, input().split())
# 초기화 필요
temp = [0] * (n * m) 
res = []
max_count = -1

for i in range(1, n+1):
  for j in range(1, m+1): 
    temp[i+j] += 1

for count in temp:
  if count > max_count:
    max_count = count

for idx, count in enumerate(temp):
  if count == max_count:
    res.append(idx)

res.sort()

for value in res:
  print(value, end=" ")


# 답안 
n, m = map(int, input().split())
cnt = [0]*(n+m+3)
max = -2147000000 

for i in range(1, n+1):
  for j in range(1, m+1):
    cnt[i+j] += 1

for i in range(n+m+1):
  if cnt[i] > max:
    max = cnt[i]

for i in range(n+m+1):
  if cnt[i] == max:
    print(i, end=' ')