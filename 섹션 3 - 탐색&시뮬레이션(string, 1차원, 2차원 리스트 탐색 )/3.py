card = list(range(21))
for _ in range(10):
  s, e = map(int, input().split())
  num = (e-s + 1)
  for i in range(0, num//2):
    card[s+i], card[e-i] = card[e-i], card[s+i]

for idx in range(1, 21):
  print(card[idx], end=" ")
  

# 강의 풀이
a = list(range(21))
for _ in range(10):
   s, e = map(int, input().split())
   for i in range((e-s+1)//2):
    a[s+i], a[e-i] = a[e-i], a[s+i]

a.pop(0)
for x in a:
   print(x, end=' ')


# 다른 풀이
card = list(range(21))

for _ in range(10):
    s, e = map(int, input().split())
    card[s:e+1] = card[s:e+1][::-1]

for idx in range(1, 21):
    print(card[idx], end=" ")