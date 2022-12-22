# 내 답안

import sys

n, m = map(int, sys.stdin.readline().split())
result = []

for i in range(0, n, 1):
  num_zip = list(map(int, sys.stdin.readline().split()))
  num_zip.sort()
  result.append(num_zip[0])

result.sort()
print(result[-1])

# 책 답안
n, m = map(int, input().split())

result = 0

for i in range(n):
  data = list(map(int, input().split()))
  min_value = min(data)
  result = max(result, min_value)

print(result)
