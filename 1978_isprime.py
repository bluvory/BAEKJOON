# 소수 찾기

def isprime(n):
  cnt = 0
  for i in range(1, n+1):
    if n % i == 0:
      cnt += 1
  if cnt == 2:
    return True

n = int(input())
data = list(map(int, input().split()))
res = 0

for x in data:
  if isprime(x) == True:
    res += 1

print(res)
