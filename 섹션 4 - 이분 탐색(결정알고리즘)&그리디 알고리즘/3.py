n, m = map(int, input().split())
music = list(map(int, input().split()))

def Count(value):
  count = 1
  sum = 0 
  
  for x in music:
    # if sum+x >= value:
    if sum+x > value:
      count += 1
      sum = x
    else:
      sum += x

  return count


lt = 1
rt = sum(music)
res = 0

while lt <= rt:
  mid = (lt + rt) // 2
  if Count(mid) <= m:
    res = mid
    rt = mid - 1
  else:
    lt = mid + 1
    
print(res)