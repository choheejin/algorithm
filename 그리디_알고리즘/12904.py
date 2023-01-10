# 골드 문제 처음으로 한번에 맞춰봄..!! 감격~~

import sys

S = list(sys.stdin.readline().rstrip())
T = list(sys.stdin.readline().rstrip())

result = 1

str_s = ''.join(S)

while True:
  str_t = ''.join(T)
  temp = str_t

  if str_s == str_t:
    break
  
  if T[-1] == 'A':
    del T[-1]
    str_t = ''.join(T)
    
  elif T[-1] == 'B':
    del T[-1]
    T = T[::-1]
    str_t = ''.join(T)

  if temp == str_t or len(T) <= 0:
    result = 0
    break

print(result)
