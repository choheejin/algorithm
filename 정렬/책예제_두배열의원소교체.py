# 내 답안

import sys

n, k = map(int, sys.stdin.readline().split())

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

minA = 0 
indexA = 0
maxB = 0 
indexB = 0

for i in range(k):
  minA = min(A)
  maxB = max(B)
  indexA = A.index(minA)
  indexB = B.index(maxB)
  A[indexA] = maxB
  B[indexB] = minA

print(sum(A))

# 책 답안과는 다르게 나의 답안은 B의 최대값이 A의 최소값보다 작은 경우를 생각을 하지 않았다.
# 해당 답안은 오류가 날 것.

# 책 답안
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
  if a[i] < b[i]:
    a[i], b[i] = b[i], a[i]
  else:
    break

 print(sum(a))
