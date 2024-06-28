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






