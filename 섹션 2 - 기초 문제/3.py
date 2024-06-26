n, k = map(int, input().split())
lst = list(map(int, input().split()))
sum_set = set()

for i in range(0, n-2):
  sum = 0
  for j in range(i+1, n-1):
    for l in range(j+1, n):
      sum = lst[i] + lst[j] + lst[l]
      sum_set.add(sum)  

sum_lst = sorted(sum_set, reverse=True)
print(sum_lst[k-1])

'''
n , k= map(int,input("카드 n장 k번째 수").split()) 
a = list(map(int, input("").split()))
res=set()
for i in range(n):
    for j in range(i+1,n):
        for m in range(j+1, n):
            res.add(a[i]+a[j]+a[m])
res = list(res)
res.sort(reverse=True)
print(res[k-1])
'''