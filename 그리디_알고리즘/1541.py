# 조건을 잘 읽자
# 연산자가 없을 수도 있다는 조건을 읽지 않아서 틀렸음.

import sys
import re

sentance = sys.stdin.readline().rstrip()
op = []

for alpha in sentance:
  if '-' == alpha:
    op.append('-')
  if '+' == alpha:
    op.append('+')

result = []

for i in re.split('[+-]', sentance):
  result.append(int(i))

if '-' in op:
  index = op.index('-')
  for i in range(index, len(op)):
    op[i] = '-'

count = 0
total = 0

if len(op) == 0:
  print(result[0])
else:
  for i in range(len(op)):
    if i == 0:
      total = result[i]
    if op[i] == '-':
      total = total - result[i+1]
    else:
      total = total + result[i+1]
  
  print(total)
