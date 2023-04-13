# 프로그래머스 올바른 괄호
def solution(s):
    left = 0
    right = 0
    for i in s:
        if i == '(':
            left += 1
        else:
            right += 1
    if left == right:
        answer = True
    else:
        answer = False
    return answer
    
def solution(s):
    answer = True
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        elif len(stack) and i == ')':
            stack.pop()
        else:
            return False
    return False if len(stack) else True
