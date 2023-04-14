# 틀림
word = list(input())
left, middle, right = [], [], []

for i in word:
    if i in middle:
        right.append(i)
        left.append(i)
        middle.remove(i)
    else:
        middle.append(i)

if len(middle)>1:
    print("I'm Sorry Hansoo")
else:
    print(''.join(left)+''.join(middle)+''.join(reversed(right)))
    
# 왜틀렸냐면... 모르겟음
# collections.Counter 써서 하기
import collections

word = list(input())
check_word = collections.Counter(word)
cnt = 0
result = ''
mid = ''

for word, num in list(check_word.items()):
    if num%2 == 1:
        cnt += 1
        mid = word
        # 홀수 두개면 못함
        if cnt >= 2:
            print("I'm Sorry Hansoo")
            break

for word, num in sorted(check_word.items()):
    result += (word*(num//2))

if cnt < 2:
    print(result+mid+result[::-1])
