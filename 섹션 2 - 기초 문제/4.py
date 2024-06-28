n = int(input("몇 명? : "))
scores = list(map(int, input().split()))

avg = sum(scores) / n
avg = round(avg)

min = 100
order = 0

for idx, value in enumerate(scores):
  if abs(avg - value) < min:
    if min < value:
      min = value
      order = idx + 1

print(min, order, sep=" ")    





