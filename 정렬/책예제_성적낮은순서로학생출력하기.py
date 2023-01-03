# 내 답안

import sys

n = int(sys.stdin.readline())
data = []

for _ in range(n):
  name, score = sys.stdin.readline().split()
  data.append([name, int(score)])

data.sort(key=lambda x:x[1])

for i in data:
  print(i[0], end=' ')
  
