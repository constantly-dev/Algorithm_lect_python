n = int(input())
lst = list(map(int, input().split()))

def reverse(x):
  x_list = list(str(x))
  temp = []
  for i in range(len(x_list)):
      top = x_list.pop()
      temp.append(top)
  reversed_str = ''.join(temp)
  return int(reversed_str)

def isPrime(x):
  if x<2:
    return False
  for i in range(2, x):
    if x % i == 0:
      return False
  return True

for i in lst:
  reverse_val = reverse(i)
  if isPrime(reverse_val):
    print(reverse_val, end=' ')