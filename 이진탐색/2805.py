# 책 예제 문제랑 똑같았어서 풀 수 있었음.
# 아직 이분 탐색 문제에 대한 감이 부족한 것 같음.

import sys

n, m = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(array)

result = 0

while start <= end:
  total = 0
  mid = (start + end) // 2
  for x in array:
    if x > mid:
      total += x - mid

  if total < m:
    end = mid - 1
  else:
    result = mid
    start = mid + 1

print(result)
