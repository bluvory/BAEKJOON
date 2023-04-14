word = list(input())
left, middle, right = [], [], []

for i in word:
    if i in middle:
        right.append(i)
        left.append(i)
        middle.remove(i)
    else:
        middle.append(i)

if len(middle)>2:
    print("I'm Sorry Hansoo")
else:
    print(''.join(left)+''.join(middle)+''.join(reversed(right)))
