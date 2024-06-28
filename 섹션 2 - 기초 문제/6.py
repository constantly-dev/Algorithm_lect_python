n = int(input())
lst = list(map(int, input().split()))

sum_lst = []

for idx, entire in enumerate(lst):
  num_sum = 0
  for i in str(entire):
    num_sum += int(i)
  sum_lst.append((idx, num_sum))

max_value = -1

for i in sum_lst:
  if i[1] > max_value:
    max_value = i[1]
    temp_idx = i[0]

print(lst[temp_idx])


# 답안1 (강의 풀이)
n = int(input())
a = list(map(int, input().split()))

def digit_sum(x):
  sum = 0
  while x>0: 
    sum += x%10
    x = x//10
  return sum

max = -2147000000
for x in a:
  tot = digit_sum(x)
  if tot > max:
    max = tot
    res = x

print(res)

# 답안2 (강의 풀이)
n = int(input())
a = list(map(int, input().split()))

def digit_sum(x):
  sum = 0
  for i in str(x):
    sum += int(i)
  return sum

max = -2147000000
for x in a:
  tot = digit_sum(x)
  if tot > max:
    max = tot
    res = x

print(res)
