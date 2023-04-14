# 프로그래머스 스킬체크테스트4 틀림
import itertools
import math

def solution(n, edges):
    answer = 0
    edge_dic = {n+1:[] for n in range(n)}
    for edge in edges:
        for i in range(n):
            edge_dic[edge[0]].append(edge[1])
            edge_dic[edge[1]].append(edge[0])
    for j in edge_dic.keys():
        edge_dic[j] = set(edge_dic[j])
        
    dist_f = []
    com = list(itertools.combinations(edge_dic.keys(), 3))
    for i in range(len(com)):
        ab = get_dist(com[i][0:2], edge_dic)
        bc = get_dist(com[i][1:], edge_dic)
        ca = get_dist(tuple([com[i][j] for j in (0, -1)]), edge_dic)
        dist_f.append((ab+bc+ca)/3)
    
    return max(dist_f)

def get_dist(com_tuple, edge_dic):
    dist = 0
    a = com_tuple[0]
    b = com_tuple[1]
    while True:
        if b in edge_dic[a]:
            dist += 1
            break
        else:
            a = list(edge_dic[a])[-1]
            dist += 1
    return dist
