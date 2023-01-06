import sys

n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))

n_list.sort()

def binary_search(array, target):
  start = 0
  end = len(array) - 1
  
  while start <= end:
    mid = (start + end) // 2
    if array[mid] == target:
      return 1
    else:
      if array[mid] > target:
        end = mid - 1
      else:
        start = mid + 1
  
  return 0

for i in m_list :
  print(binary_search(n_list, i), end=' ')
