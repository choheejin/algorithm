import sys

n = int(sys.stdin.readline())

num_zip = []

for i in range(n):
  num = int(sys.stdin.readline())
  if(num == 0 and len(num_zip) > 0):
    num_zip.pop()
  elif(num != 0):
    num_zip.append(num)

result = 0

for num in num_zip:
  result = result + num

print(result)
    

# 다른 사람 코드 보고 코드 최적화 -> 불필요한 for 문 제거
import sys

n = int(sys.stdin.readline())

num_zip = []

for i in range(n):
  num = int(sys.stdin.readline())
  if(num == 0 and len(num_zip) > 0):
    del num_zip[-1]
  elif(num != 0):
    num_zip.append(num)

print(sum(num_zip))
