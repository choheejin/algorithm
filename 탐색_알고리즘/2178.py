# dfs 로 하려다가 dfs는 최적의 경로를 보장하지 않는다는 걸 깨닳음..

from collections import deque
import sys

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
  queue = deque()
  queue.append((x, y))

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = dx[i] + x
      ny = dy[i] + y
      if nx >= n or ny >= m or nx < 0 or ny <0 :
        continue
      if graph[nx][ny] == 1:
        queue.append((nx, ny))
        graph[nx][ny] = graph[x][y] + 1

n, m = map(int, sys.stdin.readline().split())
graph = []

for _ in range(n):
  graph.append(list(map(int, sys.stdin.readline().rstrip())))

bfs(0, 0)
print(graph[n-1][m-1])
