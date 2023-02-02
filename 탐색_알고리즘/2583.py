# 예제는 맞는데 왜 틀린지 모르겠다..
import sys

sys.setrecursionlimit(10 ** 5)

m, n, k = map(int, sys.stdin.readline().split())

def dfs(array, x, y):
  global count
  if x < 0 or x >= n or y < 0 or y >= m:
    return False
  if array[y][x] == 0:
    array[y][x] = 1
    count += 1
    dfs(array, x+1, y)
    dfs(array, x-1, y)
    dfs(array, x, y+1)
    dfs(array, x, y-1)
    return True
  return False


array = [[0 for _ in range(n)] for _ in range(m)]
result = []
count = 0

for _ in range(k):
  x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
  
  for i in range(y1, y2):
    for j in range(x1, x2): 
      array[i][j] += 1

for a in range(m):
  for b in range(n):
    if dfs(array, a, b) == True:
      result.append(count)
    else:
      count = 0
    
print(len(result))
print(*sorted(result))

# 다른 사람 풀이
import sys
sys.setrecursionlimit(10000)

def dfs(y, x, cnt):
    graph[y][x] = 1
    for dy, dx in d:
        Y, X = y+dy, x+dx
        if (0 <= Y < M) and (0 <= X < N) and graph[Y][X] == 0:
            cnt = dfs(Y, X, cnt+1)
    return cnt
    
M, N, K = map(int, input().split())
graph = [[0]*N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
res = []
for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            res.append(dfs(i, j, 1))
print(len(res))
print(*sorted(res))

