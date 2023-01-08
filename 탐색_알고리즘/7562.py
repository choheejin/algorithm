# 쉽게 풀 수 있었음

import sys
from collections import deque

graph = []
 
dx = [1, -1, 2, -2, 1, -1, 2, -2]
dy = [2, 2, 1, 1, -2, -2, -1, -1]

def bfs(x, y, x2, y2, visited, m):
  queue = deque()
  queue.append((x, y))
  
  visited[x][y] = 1
  
  while queue:
    x, y = queue.popleft()
    if x == x2 and y == y2:
      return visited[x][y]
    
    for i in range(8):
      nx = dx[i] + x
      ny = dy[i] + y
      if nx<0 or nx >= m or ny<0 or ny>=m:
        continue
      
      else:
        if visited[nx][ny] == 0:
          visited[nx][ny] = visited[x][y] + 1
          queue.append((nx, ny))
  return 0
  
t = int(sys.stdin.readline())
result = []
for _ in range(t):
  I = int(sys.stdin.readline())
  visited = [[0 for _ in range(I)] for _ in range(I)]
  s_x, s_y = map(int, sys.stdin.readline().split())
  t_x, t_y = map(int, sys.stdin.readline().split())
  result.append(bfs(s_x, s_y, t_x, t_y, visited, I))

for i in result:
  print(i-1)

  
