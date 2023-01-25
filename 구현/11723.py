# 처음 구현 성공 후, 시간 줄이기에 초점을 맞춤.
# 최종으로 고쳐도 최적의 시간이 안 나와서 다른 사람 코드 참고함.
# 내 코드 30616kb	3952ms

import sys

n = int(sys.stdin.readline())
s = set()

for _ in range(n):
  op = sys.stdin.readline().rstrip()
  
  if op == 'all':
    s = {i for i in range(1, 21)}
    continue
  elif op == 'empty':
    s = set()
    continue
  
  op, x = op.split(' ')
  x = int(x)
  
  if op == 'add':
    s.add(x)
  elif op == 'remove':
    s.discard(x)
  elif op == 'check':
    if x in s:
      print(1)
    else:
      print(0)
  elif op == 'toggle':
    if x in s:
      s.remove(x)
    else:
      s.add(x)


# 다른 사람 코드 30616kb	3312ms

import sys

M = int(input())
S = 0

for _ in range(M):
    o = sys.stdin.readline().split()
    if o[0] == "add":
        S |= (1 << int(o[1]))
    elif o[0] == "remove":
        S &= ~(1 << int(o[1]))
    elif o[0] ==  "check":
        print(1 if S & (1 << int(o[1])) else 0)
    elif o[0] == "toggle":
        S ^= (1 << int(o[1]))
    elif o[0] == "all":
        S = (2 ** 21) - 1
    else:
        S = 0
