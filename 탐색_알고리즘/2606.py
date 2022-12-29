# 감격 그 잡채...
import sys

count = 0

def dfs(graph, v, visited):
  global count
  visited[v] = True
  count = count + 1
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for i in range(n+1)]

visited = [False] * (n+1)

for i in range(m):
  n, m = map(int, sys.stdin.readline().split())
  graph[n].append(m)
  graph[m].append(n)

dfs(graph, 1, visited)
print(count - 1)
