# 감 떨어지면 좀 어렵다는 걸 느낌..
# 자주 풀어야겠다!

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

start = 0

for i in range(m):
  x, y = map(int, sys.stdin.readline().split())
  if i == 0:
    start = x
  graph[x].append(y)
  graph[y].append(x)

def bfs(x):
  queue = deque()
  queue.append(x)
  visited[x] = True
  while queue:
    v = queue.popleft()
    for i in graph[v]:
      if not visited[i]:
        visited[i] = True
        queue.append(i)

count = 0
visited[0] = True

while True:
  if False in visited:
    notvisited = visited.index(False)
    count += 1
    bfs(notvisited)
  else:
    break

print(count )
