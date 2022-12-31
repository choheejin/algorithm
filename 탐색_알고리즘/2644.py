# 짱 어려웠다..
# 탐색을 그만 두는 조건 및 리프노드까지 탐색을 해서 돌아올 때의 카운트 감소 부분이 어려웠음..

import sys
from collections import deque

sys.setrecursionlimit(100000)

count = 0
flag = False

def dfs(x, y):
  global count, flag

  if flag :
    return

  visited[x] = True
  count = count + 1
  
  for i in graph[x]:
    if not visited[i]:
      if i == y:
        flag = True
        return
      dfs(i, y)
  if flag == False:
    count = count - 1 
  
n = int(sys.stdin.readline())
ans_x , ans_y = map(int, sys.stdin.readline().split())
edge = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(edge):
  x, y = map(int, sys.stdin.readline().split())
  graph[x].append(y)
  graph[y].append(x)

dfs(ans_x, ans_y)

if flag == True:
  print(count)
else:
  print(-1)
