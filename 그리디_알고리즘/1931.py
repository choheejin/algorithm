import sys

n = int(sys.stdin.readline())

room = []

for i in range(n):
  x, y = map(int, sys.stdin.readline().split())
  room.append([x,y])

room.sort(key=lambda x:x[0])
room.sort(key=lambda x:x[1])

pre = 0
count = 0

for i in room:
  if(pre <= i[0]):
    count = count + 1
    pre = i[1]
    
print(count)

# 검색해서 문제 풀 수 있었음
# 내가 찾지 못했던 포인트 : 시작 시간을 먼저 정렬해주고 -> 끝나는 시간을 정렬해줬어야함
# 끝나는 시간을 먼저 정렬했다가 계속 문제가 풀리지 않았음

# 시작 시간을 먼저 정렬해줬어야 하는 이유
# 끝나는 시간 기준으로만 정렬하면, 시작 시간이 빠르고, 끝나는 시간도 적당히 빠르지만 뒤에 있어서 카운트 되지 않는 경우도 존재할 거 같기 때문..?
