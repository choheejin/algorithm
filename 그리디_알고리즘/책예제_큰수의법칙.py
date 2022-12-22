# 나의 답안

import sys

n, m, k = map(int, sys.stdin.readline().split())
num_zip = list(map(int, sys.stdin.readline().split()))

count = 0
result = 0
num_zip.sort(reverse=True)

for i in range(0, m, 1):
  if(count >= k):
    result = result + num_zip[1]
    count = 0
  else:
    result = result + num_zip[0]
  count = count + 1

print(result)

# 책의 답안

n,m,k = map(int, input().split())
data = list((map(int, input().split())))

data.sort()
first = data[n-1]
second = data[n-2]

count = int(m/(k+1)) * k
count += m % (k+1)

result = 0
result += (count) * first
result += (m - count) * second

print(result)
