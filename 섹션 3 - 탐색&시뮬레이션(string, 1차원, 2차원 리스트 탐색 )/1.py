n = int(input())

# 파이썬스러운 코드
for i in range(n):
  s = input()
  s = s.upper()
  if s == s[::-1]:
    print("#%d YES" %(i+1))
  else:
    print("#%d NO" %(i+1))

# 직접 비교
n = int(input())
for i in range(n):
  s = input()
  s = s.upper()

  size = len(s)
  for j in range(size//2):
    if s[j] != s[-1-j]:
      print("#%d NO" %(i+1))
      break
  else:
    print("#%d YES" %(i+1))

# 스택을 이용해 본다면?
n = int(input())
for i in range(n):
  s = input()
  s = s.upper()

  temp = []
  for letter in s:
    temp.append(letter)
  
  isPalindrome = False
  for letter in s:
    if temp.pop() != letter:
      isPalindrome = False
      break
  else:
    isPalindrome = True
  
  if isPalindrome:
    print("#%d YES" %(i+1))
  else:
    print("#%d NO" %(i+1))



