# 내 답안
import sys

n = int(sys.stdin.readline())
paths = list(sys.stdin.readline().split())

i = 1
j = 1

for path in paths:
  if(path == 'R'):
    if(j+1 <= n):
      j = j + 1
  if(path == 'U'):
    if(i-1 >= 1 ):
      i = i - 1
  if(path == 'D'):
    if(i+1 <= n):
      i = i + 1
  if(path == 'L'):
    if(j-1 >= 1):
      j = j - 1

print(i, j)

# 책 답안
n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
      continue
    x, y = nx, ny

print(x, y)
