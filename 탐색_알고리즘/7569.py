# 그냥 3차원 배열로 생각하고 풀었으면 어떻게든 성공했을거 같은데...
# 너무 어렵게 접근함 다음부턴 좀 더 단순하게 가자!

# 내 코드 

import sys
from collections import deque

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

count = -1


def bfs(x, y, z):
  queue = deque()
  queue.append((x, y, z))
  global count
  
  while queue:
    x, y, z = queue.popleft()
    # z 좌표 계산: N * z + 1
    count = count + 1
    for i in range(6):
      nx = dx[i] + x
      ny = dy[i] + y
      nz = dz[i] + z
      locY = ny + N*nz + 1
      if nx >= M or nx < 2 or ny >= N or ny < 2 or nz >= H or nz < 1:
        continue
      
      if visited[nx][locY] == 0 and box[nx][locY] == 0:
        box[nx][locY] = 1
        visited[nx][locY] = visited[x][y+ N*z+1] + 1
        queue.append((nx, ny, nz))
      
  
    
M, N, H = map(int, sys.stdin.readline().split())

visited = [[0] for _ in range(N*H)]

box = []

indexX = -1
indexYZ = -1

for i in range(N*H):
  tomatos = list(map(int, sys.stdin.readline().split()))
    
  if(1 in tomatos):
    indexX = tomatos.index(1)
    indexYZ = i
  
  box.append(tomatos)

if indexX != -1 and indexYZ != -1:
  bfs(indexX, indexYZ%N - 1, indexYZ//N)
  print(count)
  print(indexX, indexYZ%N - 1, indexYZ//N)
else:
  print(-1)

# 구글링
import sys
from collections import deque
m,n,h = map(int,input().split()) # mn크기, h상자수
graph = []
queue = deque([])
 
for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int,sys.stdin.readline().split())))
        for k in range(m):
            if tmp[j][k]==1:
                queue.append([i,j,k])
    graph.append(tmp)
    
dx = [-1,1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]
while(queue):
    x,y,z = queue.popleft()
    
    for i in range(6):
        a = x+dx[i]
        b = y+dy[i]
        c = z+dz[i]
        if 0<=a<h and 0<=b<n and 0<=c<m and graph[a][b][c]==0:
            queue.append([a,b,c])
            graph[a][b][c] = graph[x][y][z]+1
            
day = 0
for i in graph:
    for j in i:
        for k in j:
            if k==0:
                print(-1)
                exit(0)
        day = max(day,max(j))
print(day-1)
  
