# 결과 정렬 안해서 틀림
# 문제를 꼼꼼히 읽자 !!

import sys

count = 0

def dfs(x, y):
  global count
  if x <= -1 or x >= n or y <= -1 or y >= n:
    return False
  if graph[x][y] == 1:
    graph[x][y] = 0
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)
    count = count + 1
    return True
  return False

n = int(sys.stdin.readline())
graph = []

for i in range(n):
  graph.append(list(map(int, sys.stdin.readline().rstrip())))

result_count = []
result = 0
for i in range(n):
  for j in range(n):
    if dfs(i, j) == True:
      result_count.append(count)
      count = 0
      result = result + 1

result_count.sort()

print(result)
for i in result_count:
  print(i)

