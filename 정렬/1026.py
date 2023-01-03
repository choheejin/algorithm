import sys

n = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))


A.sort()
B.sort(reverse=True)

data = 0

for i in range(n):
  data = data + (A[i]*B[i])

print(data)
