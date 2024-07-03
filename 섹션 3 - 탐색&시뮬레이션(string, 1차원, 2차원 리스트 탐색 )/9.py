n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

a.insert(0, [0] * n)
a.append([0] * n)

for x in a:
  x.insert(0, 0)
  x.append(0)

count = 0

for idx_r, value_r in enumerate(a):
  for idx_c, value_c in enumerate(value_r):
    if idx_r > 0 and idx_r < n+1 and idx_c > 0 and idx_c < n+1:
      if a[idx_r][idx_c] > a[idx_r-1][idx_c] and\
          a[idx_r][idx_c] > a[idx_r+1][idx_c] and\
              a[idx_r][idx_c] > a[idx_r][idx_c-1] and \
                a[idx_r][idx_c] > a[idx_r][idx_c+1]:
        count += 1
    
print(count)


# 강의 풀이

# naming이 x,y보다는 r,c로
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

a.insert(0, [0] * n)
a.append([0] * n)

for x in a:
  x.insert(0, 0)
  x.append(0)

cnt = 0

for i in range(1, n+1):
  for j in range(1, n+1):
    if all(a[i][j] > a[i+dr[k]][j+dc[k]] for k in range(4)):
      cnt += 1


print(cnt)
