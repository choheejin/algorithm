# 내 답안

import sys

n = int(sys.stdin.readline())
data = []

for _ in range(n):
  data.append(int(sys.stdin.readline()))

data.sort(reverse=True)

for i in range(n):
  print(data[i], end=' ')

  
# 기본적인 정렬을 할 수 있는지에 대해 물어보는 문제였다. -> 기본 정렬 라이브러리 사용하는게 
