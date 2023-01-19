# 위에랑만 비교하면 될 줄 알았지..ㅠ
# 생각해보니 아래 걸 선택하는게 훨씬 유용할때가 있구나 싶다..
## 이걸 구현을 어떻게 해야할지 몰라서 정답 찾아봄 ㅎ

import sys

n = int(sys.stdin.readline())

r = []
g = []
b = []

d = [0] * n

for i in range(n):
  x, y, z = map(int, sys.stdin.readline().split())
  r.append(x)
  g.append(y)
  b.append(z)

d[0] = min(r[0], g[0], b[0])

if d[0] == r[0]:
  pre_color = 'r'
elif d[0] == g[0]:
  pre_color = 'g'
else:
  pre_color = 'b'

for i in range(1, n, 1):
  if pre_color == 'r':
    d[i] = min(g[i], b[i])
    if d[i] == g[i]:
      pre_color = 'g'
    else:
      pre_color = 'b'
  elif pre_color == 'g':
    d[i] = min(r[i], b[i])
    if d[i] == r[i]:
      pre_color = 'r'
    else:
      pre_color = 'b'
  else:
    d[i] = min(r[i], g[i])
    if d[i] == r[i]:
      pre_color = 'r'
    else:
      pre_color = 'g'

print(sum(d))

# 구글링

n = int(input())
p = []
for i in range(n):
    p.append(list(map(int, input().split())))
for i in range(1, len(p)):
    p[i][0] = min(p[i - 1][1], p[i - 1][2]) + p[i][0]
    p[i][1] = min(p[i - 1][0], p[i - 1][2]) + p[i][1]
    p[i][2] = min(p[i - 1][0], p[i - 1][1]) + p[i][2]
print(min(p[n - 1][0], p[n - 1][1], p[n - 1][2]))

# 음.. 구글링한 답도 이해하기 쉽지 않군 ㅋㅋㅠㅠㅠ
# 언제쯤 dp 잘 풀 수 있을까 ㅠ
