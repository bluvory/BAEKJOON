# 시간초과
now = list(input())
n = int(input())
command_list = []

for i in range(n):
    command_list.append(input())

out = now
curser = len(now)
for command in command_list:
    c = command.split()[0]
    if c == 'L' and curser != -1:
        curser -= 1
    if c == 'D' and curser != len(out):
        curser += 1
    if c == 'B' and curser != -1:
        now.remove(curser-1)
        curser += 1
    if c == 'P':
        now.insert(curser, command.split()[1])
        curser += 1
        pass

print(''.join(out))
