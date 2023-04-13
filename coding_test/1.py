# 프로그래머스 달리기경주 내풀이
def solution(players, callings):
    answer = []
    for call in callings:
        call_idx = players.index(call)
        a = players[call_idx-1]
        players[call_idx-1] = players[call_idx]
        players[call_idx] = a
        #players[call_idx-1], players[call_idx] = players[call_idx], players[call_idx-1]
    return players
