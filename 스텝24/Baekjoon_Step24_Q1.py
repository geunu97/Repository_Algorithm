#24단계: DFS와 BFS
#1. 

from collections import deque

N,M,V = map(int,input().split())

graph = [ [] for _ in range(N+1)]           #인접리스트로 그래프 그리기 (양방향)
for i in range(1,M+1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a] = sorted(graph[a])
    graph[b] = sorted(graph[b])

answer_DFS = []                             #DFS
answer_DFS.append(V)
def DFS(V):
    for i in graph[V]:
        if i not in answer_DFS:
            answer_DFS.append(i)
            DFS(i)
            
answer_BFS = []                             #BFS
answer_BFS.append(V)
q = deque(answer_BFS)
q.append(V)
def BFS(q):
    while q:
        value = q.popleft()

        for i in graph[value]:
            if i not in answer_BFS:
                answer_BFS.append(i)
                q.append(i)

DFS(V)
BFS(q)

for i in range(len(answer_DFS)):
    print(answer_DFS[i],end=" ")

print("")
for i in range(len(answer_BFS)):
    print(answer_BFS[i],end=" ")




