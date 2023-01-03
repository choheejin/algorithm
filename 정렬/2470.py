# 내 답안...
# 선택정렬처럼 풀 생각을 했지 퀵 정렬처럼 풀 생각을 전혀 하지 못했다...
# 분발하자 조희진!

import sys

n = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))

preData = 1000000000 
resultX = 0
resultY = 0

for i in range(n):
  for j in range(i+1, n):
    x = A[i]
    y = A[j]
    data = A[i] + A[j]
    if data < 0:
      data = - data
    if 0 < data < preData:
      preData = data
      if A[j] < A[i]:
        x, y = A[j], A[i]
      resultX, resultY = x, y

print(resultX, resultY)

# 구글링

# input 입력 받기
n = int(input())
solution = list(map(int, input().split(' ')))

# 정렬하기
solution.sort()

# 이중포인터 설정
left = 0
right = n-1

answer = 2e+9+1 # 기준값
final = [] # 정답

# 투포인터 진행
while left < right:
    s_left = solution[left]
    s_right = solution[right]

    tot = s_left + s_right
    # 두 용액의 합이 0과 가장 가까운 용액을 정답에 담아주기
    if abs(tot) < answer:
        answer = abs(tot)
        final = [s_left, s_right]
	
    # 두 용액의합이 0보다 작다면 왼쪽의 값을 늘려 조금 더 0에 가깝게 만들어준다
    if tot < 0:
        left += 1
    # 반대로, 두 용액의 합이 0보다 크다면 오른쪽의 값을 줄여서 조금 더 0에 가깝게 만들어준다
    else:
        right -= 1

print(final[0], final[1])
