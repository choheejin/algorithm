# 정답 봤을 때도 이해 안 간 문제...

import sys
from collections import deque

n = int(sys.stdin.readline())
table = []

for i in range(n):
  table.append(list(map(int, sys.stdin.readline().split())))

table.sort(key=lambda x: x[1], reverse=True)

room = 1
start = table[0][0]
end = table[0][1]
candidate = deque()

for i in range(1, n):
  if len(candidate) != 0:
    tmp = candidate.popleft()
    if tmp > table[i][1]:
      room -= 1
  if start < table[i][1] < end:
    room += 1
    if table[i][0] < start:
      candidate.append(start)
  start = table[i][0]
  end = table[i][1]

print(room)

# 구글링
# heap 사용하는 방법

# arr를 시작점을 기준으로 정렬을 한다.
# 존재하는 회의실의 끝나는 시간을 저장하는 heap rooms를 생성한다.
# arr를 돌면서 가장빨리 끝나는 회의실(rooms[0])과 비교한다.
# 크거나 같다면 pop한다.
# 작다면 회의실을 추가하는 것으로 answer을 더해준다.
# rooms에 추가해준다. 

# 자료구조 다시 좀 봐야겠다 ... ^_^

import sys
import heapq
input = sys.stdin.readline
 
N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
arr.sort(key=lambda x: x[0])
 
rooms = [0]
answer = 1
for s, e in arr:
    if s >= rooms[0]:
        heapq.heappop(rooms)
    else:
        answer+=1
    heapq.heappush(rooms, e)
 
print(answer)
