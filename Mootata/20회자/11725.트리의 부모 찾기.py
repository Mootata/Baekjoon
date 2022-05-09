import sys
from collections import deque

input = sys.stdin.readline

n = int(input()) # 노드의 개수 N
tree = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for _ in range(n - 1):
    n1, n2 = map(int, input().split())
    tree[n1].append(n2)
    tree[n2].append(n1)

def bfs():
    q = deque()
    q.append(1)
    answer = [0 for _ in range(n + 1)]
    
    while q:
        node = q.popleft()
        
        visited[node] = True
        for i in tree[node][:]: # 각 노드의 자식 노드
            if not visited[i]: 
                q.append(i)
                answer[i] = node
    return answer[2:]

print(*bfs(), sep='\n')