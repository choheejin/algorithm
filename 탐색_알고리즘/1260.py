# 작은 순부터 안해서 틀릴뻔~

import sys
from collections import deque

count = 0

def dfs(graph, v, visited):
  visited[v] = True
  print(v, end=' ')  
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True
  while queue:
    v = queue.popleft()
    print(v, end = ' ')
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True


n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for i in range(n+1)]

visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)


for i in range(m):
  x, y = map(int, sys.stdin.readline().split())
  graph[x].append(y)
  graph[y].append(x)
  graph[x].sort()
  graph[y].sort()


  
dfs(graph, v, visited_dfs)
print('')
bfs(graph, v, visited_bfs)
