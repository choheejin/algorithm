# 반복문 탈출 방법을 못 찾음

import sys

a, b = map(int, sys.stdin.readline().split())

count = 0
flag = 0
while a != b:
  temp = b
  if b % 10 == 1:
    b = b // 10
    count += 1
  elif b % 2 == 0:
    b = b // 2
    count += 1
  if b == temp:
    flag = 1
    break

if flag == 1:
  print(-1)
else:
  print(count+1)
