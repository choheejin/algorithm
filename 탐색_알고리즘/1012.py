# 오랜만에 그래프 탐색 문제 푸니까 감이 떨어졌다..
# 오래 안 본 문제 다시 한번 낭독해봐야겠다

import sys
sys.setrecursionlimit(10 ** 5)

t = int(sys.stdin.readline())

def dfs(array, x, y):
  if x < 0 or x >= n or y < 0 or y >= m:
    return False
  if array[x][y] == 1:
    array[x][y] = 0
    dfs(array, x-1, y)
    dfs(array, x, y-1)
    dfs(array, x+1, y)
    dfs(array, x, y+1)
    return True
  return False
      

for _ in range(t):
  m, n, k = map(int, sys.stdin.readline().split())
  array = [[0 for _ in range(m)] for _ in range(n)]

  for i in range(k):  
    y, x = map(int, sys.stdin.readline().split())
    array[x][y] = 1

  count = 0
  for a in range(n):
    for b in range(m):
      if dfs(array, a, b) == True:
        count += 1
        
  print(count)
