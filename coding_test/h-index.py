# 프로그래머스 h-index
def solution(citations):
    citations.sort(reverse=True)
    for idx, cite in enumerate(citations):
        if idx >= cite:
            return idx
    return len(citations)
