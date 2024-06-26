T = int(input("몇 번째 테스트 케이스: "))

for t in range(T):
  n, s, e, k = map(int, input().split())
  lst = list(map(int, input().split()))

  lst = lst[s-1: e]
  lst.sort()
  
  for idx, value in enumerate(sorted(lst)):
    if idx == k-1:
      print("#", end='')
      print(t+1, value, sep=' ')
      break

'''
T = int(input(""))
for t in range(T):
  n, s, e, k = map(int, input().split())
  a = list(map(int, input().split()))
  a = a[s-1:e]
  a.sort()
  print("#%d %d" %(t+1, a[k-1]))
'''
