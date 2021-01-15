import sys
input = sys.stdin.readline

n = int(input())
arr = [input() for _ in range(n)]
res = ""

for i in zip(*arr):
  if len(set(i)) == 1:
    res += i[0]
    print(set(i), res, i[0])
  else:
    res += "?"

print(res)

# n = 3
# arr = [config.sys, config.inf, configures]
# zip(*arr) = [(c,c,c), (o,o,o), ..., (s,f,s)]
# set(i) = 집합자료형으로 중복제거
# if len(set(i)) == 1 : 중복제거했을때 1 즉 같은 문자 세개
