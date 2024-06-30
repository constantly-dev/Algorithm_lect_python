s = input()
temp = []

for value in s:
  if value.isdigit():
    temp.append(value)

res = int(''.join(temp))

count = 0

for i in range(1, res+1):
  if res % i == 0:
    count += 1

print(res)
print(count)


# 강의 풀이
s = input()
res = 0 

for x in s:
  if x.isdecimal():
    res = res*10 + int(x)

print(res)

cnt = 0
for i in range(1, res+1):
  if res % i == 0:
    cnt += 1

print(cnt)
