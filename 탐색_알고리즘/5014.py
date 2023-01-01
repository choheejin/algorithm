# 처음 노드를 방문했다고 취급하지 않아서 1000000 1000000 1 0 1 를 제대로 테스트하지 못함

import sys
from collections import deque

def bfs(S, G):  
  queue = deque()
  queue.append(S)
  visited[S] = 1
  
  while queue:
    v = queue.popleft()

    if v == G :
      return visited[v]
    
    for next in (v + U, v - D):
      if next > F or next < 1:
        continue
      
      if visited[next] == 0:
        queue.append(next)
        visited[next] = visited[v] + 1

  return -1

F, S, G, U, D = map(int, sys.stdin.readline().split())
visited = [0] * 1000001

if S == G:
  print(0)
else:
  result = bfs(S, G)
  
  if result != -1:
    print(result - 1)
  else:
    print("use the stairs")
