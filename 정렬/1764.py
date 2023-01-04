# 시간초과가 계속 나서 이유를 찾아보니 중복 제거를 위해 set을 사용해야하는 것을 알아냄

import sys

n, m = map(int, sys.stdin.readline().split())

see = set(sys.stdin.readline().rstrip() for _ in range(n))
hear = set(sys.stdin.readline().rstrip() for _ in range(m))

result = list(see & hear)
result.sort()

print(len(result))

for i in result:
  print(i)
