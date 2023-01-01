import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

flag = False

depth = []

count = 0

queue = deque()
queue.append([n])

if n == k:
  flag = True

while not flag and count < 100000:
  node = queue.popleft()
  count = count + 1
  for j in node:
    if j == k:
      flag = True
      break
    type1 = j - 1
    type2 = j + 1
    type3 = 2 * j
    queue.append([type1, type2, type3])

print(int(count ** (1/2)))


import sys
from collections import deque

def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if v == k:
            return array[v]
        for next_v in (v-1, v+1, 2*v):
            if 0 <= next_v < MAX and not array[next_v]:
                array[next_v] = array[v] + 1
                q.append(next_v)


MAX = 100001
n, k = map(int, sys.stdin.readline().split())
array = [0] * MAX
print(bfs(n))
