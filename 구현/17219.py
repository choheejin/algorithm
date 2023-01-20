# 리스트로 풀었다가 시간초과가 남
# 딕셔너리로 해야지 빨라진다. 왜지..?

# set, dict은 해시함수를 이용한 해시값을 저장하고있는 해시테이블이란 자료구조를 사용하기 때문에, 빠른 탐색이 가능함. 
# 해시는 임의의 변수(문자열 등)를 숫자로 변환하여, 매핑하는 것을 의미함. 
# 따라서, 임의의 변수가 오더라도 숫자로 매핑할 수 있고, 이 숫자로 매핑한 경우 인덱스처럼 사용할 수 있어 빠른 검색이 가능함.

import sys

n, m = map(int, sys.stdin.readline().split())

site = {}

for i in range(n):
  x, y = sys.stdin.readline().split()
  site[x] = y

for i in range(m):
  target = sys.stdin.readline().rstrip()
  print(site[target])
