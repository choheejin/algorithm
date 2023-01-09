# 내 풀이

import sys

t = int(sys.stdin.readline())

for _ in range(t):
  n = int(sys.stdin.readline())
  count = 0
  
  data = {}
  
  for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    data[x] = y

  sort_data = dict(sorted(data.items()))

  for idx in range(n, 1, -1):
    tmp = {key: value for key, value in sort_data.items() if key < idx}

    min_value = min(tmp.values())
    max_value = min(tmp.values())

    if max_value == sort_data[idx]:
      count += 1
      
    elif sort_data[idx] > min_value:
      count += 1 
    
  print(n - count)
  
# 구글링
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  N = int(input())
  rank = [list(map(int, input().split())) for _ in range(N)]
  rank_asc = sorted(rank)
  print(rank_asc)
  top = 0
  result = 1
  
  for i in range(1, len(rank_asc)):
    if rank_asc[i][1] < rank_asc[top][1]:
      top = i
      result += 1

  print(result)

# 모든 인덱스에 대해서 다 도는 것이 아닌, 한번만에 위에보다 작은 것을 골라는 방식으로!
# 문제를 처음 접근하는 방식이 잘못 되었었다.
# 그리디인 걸 유념하자!
