# 내 답안

import sys

def binary_search(array, target, start, end):
  if start > end:
    return 'no'

  mid = (start + end) // 2

  if array[mid] == target:
    return 'yes'
  elif array[mid] > target:
    return binary_search(array, target, start, mid-1)
  else:
    return binary_search(array, target, mid+1, end)

n = int(sys.stdin.readline())
products = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
clients = list(map(int, sys.stdin.readline().split()))

for item in clients:
  print(binary_search(products, item, 0, n-1), end=" ")
  
# 책에 있는 다양한 답안

# 계수 정렬 이용
n = int(input())
array = [0] * 1000001

for i in input().split():
  array[int(i)] = 1

m = int(input())

x = list(map(int, input().split()))

for i in x:
  if array[i] == 1:
    print('yes', end='')
  else:
    print('no', end='')
    

# 집합 자료형 이용
n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
  if i in array:
    print('yes', end=' ')
  else:
    print('no', end=' ')
