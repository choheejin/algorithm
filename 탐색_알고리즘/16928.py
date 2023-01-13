# 좌절..

import sys
from collections import deque

# 1~10

def bfs():
  count = 0
  queue = deque()
  queue.append((1, 0))
  visited[1] = 1
  
  while queue:
    v, store = queue.popleft()
    for i in v+1, v+2, v+3, v+4, v+5, v+6:
      # print(i)
      if i > 100:
        continue
      if visited[i] == 1:
        if 1 <= 100 - i <= 6:
          queue.append((i, 0))
        else:
          if i in snack:
            queue.append((snack[i], visited[v]))
          elif i in lader:
            queue.append((lader[i], visited[v]))
          else:
            queue.append((i, 0))
        visited[i] = visited[v] + 1 + store
        if visited[i] == 100:
          return
        # print(i, v, store)

n, m = map(int, sys.stdin.readline().split())

snack = {}
lader = {}

visited = [1 for _ in range(101)]

for i in range(n):
  x, y = map(int, sys.stdin.readline().split())
  lader[x] = y

for i in range(m):
  x, y = map(int, sys.stdin.readline().split())
  snack[x] = y

bfs()
print(visited[100] -1)
# print(visited)


# 구글링
# 간선을 이용할 생각을 왜 못했을까...?
# 두개를 따로 분리해서 보면, 사다리가 더 안 좋을 경우도 있기 때문에 안됨
# 하나로 관리해서 그래프에서의 edge 처럼 했어야만...

from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
visited = [True] + [False]*100
q = deque([(1,0)])
link = [0]*101
for _ in range(n+m):
    a,b = map(int,input().split())
    link[a]=b

while q:
    v,t = q.popleft()
    if v == 100:
        print(t)
        break
    t+=1
    for i in range(1,7):
        to_v = v+i
        if to_v > 100 or visited[to_v]:
            continue
        visited[to_v] = True
        if link[to_v]:
            q.append((link[to_v],t))
        else:
            q.append((to_v,t))
