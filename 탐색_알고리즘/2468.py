# sys.setrecursionlimit()을 추가해주지 않으면 runtime 에러 뜬다
# 공식 도큐먼트에 의하면 해당 코드는 파이썬 인터프리터 stack에 최대 깊이를 지정하는 것이다. 무한대의 recursion이 발생해서 overflow가 발생하는 것을 방지하기 위함이다.

import sys
from collections import deque

sys.setrecursionlimit(100000)

def dfs(x, y, visited, high):  
  if x >= n or y >= n or x < 0 or y < 0:
    return False
  if graph[x][y] > high and visited[x][y] == False:
    visited[x][y] = True
    dfs(x-1, y, visited, high)
    dfs(x, y-1, visited, high)
    dfs(x+1, y, visited, high)
    dfs(x, y+1, visited, high)
    return True
  return False

n = int(sys.stdin.readline().rstrip())
graph = []

for _ in range(n):
  graph.append(list(map(int, sys.stdin.readline().split())))

count = 0
result = []

for high in range(0, 101):
  visited = [[False for _ in range(n)] for _ in range(n)]
  for i in range(n):
    for j in range(n):
      if dfs(i, j, visited, high) == True:
        count = count + 1
  result.append(count)
  count = 0
  
print(max(result))

