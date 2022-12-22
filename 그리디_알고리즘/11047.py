import sys

n, k = map(int, sys.stdin.readline().split())

data = k
money_kind = []

count = 0

for i in range(n):
  money_kind.append(int(sys.stdin.readline()))

money_kind.sort(reverse=True)

for i in money_kind:
  i = int(i)
  if(i<=data):
    count = count + (data // i)
    data = data % i
    
print(count)
