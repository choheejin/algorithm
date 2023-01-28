# 내 코드

import sys

# 도감 수록 포켓몬 : n
# 맞춰야 하는 문제 : m
n, m = map(int, sys.stdin.readline().split())

dic = dict()
reverse_dic = dict()


for i in range(1, n+1):
  x = sys.stdin.readline().rstrip()
  dic[x] = i
  reverse_dic[i] = x

for _ in range(m):
  y = sys.stdin.readline().rstrip()
  try:
    index = int(y)
    print(reverse_dic[index])
  except:
    print(dic[y])
    
# 조금 더 빠른 다른 사람 코드
# 조금 아쉽구려
import sys
input = sys.stdin

M, q = map(int, input.readline().split())
pokemon = {}
reverse = {}

for i in range(M):
    text = input.readline().rstrip()
    pokemon[i+1] = text
    reverse[text] = i+1

for _ in range(q):
    x = input.readline().rstrip()
    if x[0] in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
        x = int(x)
        print(pokemon[x])
    else:
        print(reverse[x])
