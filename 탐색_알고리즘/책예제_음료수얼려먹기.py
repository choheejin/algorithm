# 못 풀었습니다... ㅠ

# 책 답안
n, m = map(int, input().split())

graph = []

for i in range(n):
  graph.append(list(map(int, input())))

def dfs(x, y):
  if x <= -1 or x >= n or y <= -1 or y >= m:
    return False
  if graph[x][y] == 0:
    graph[x][y] = 1
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)
    return True
  return False

result = 0

for i in range(n):
  for j in range(m):
    if dfs(i, j) == True:
      result += 1

print(result)

# 이론은 알지만, 코드의 동작 방식에 대해 완벽히 이해하지 못해, 응용을 못하는 것 같다.
# 자세히 코드를 뜯어보는 시간이 필요하다.
