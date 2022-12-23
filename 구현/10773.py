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
    
