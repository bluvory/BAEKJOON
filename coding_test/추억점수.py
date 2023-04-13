# 프로그래머스 추억점수
def solution(name, yearning, photo):
    answer = []
    dic = {name:yearning for name, yearning in zip(name, yearning)}
    for p in photo:
        res = 0
        for i in p:
            if i in dic.keys():
                res += dic[i]
        answer.append(res)
    return answer
