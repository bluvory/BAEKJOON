# 프로그래머스 스킬체크테스트4 런타임에러남 ;;
def solution(words, queries):
    answer = []
    
    for query in queries:
        res = 0
        for word in words:
            q = list(query)
            w = list(word)
            a = 0
            for i in range(len(q)):
                if q[i] != '?':
                    if q[i] == w[i]:
                        a += 1
            if len(query.replace('?','')) == a and len(query)==len(word):
                res +=1
        answer.append(res)
    return answer
