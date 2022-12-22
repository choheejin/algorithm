import sys

n = map(int, sys.stdin.readline().split())

num_zip = list(map(int, sys.stdin.readline().split()))

num_zip.sort()

data = 0
result_zip = []

for i in num_zip:
  data = data + i
  result_zip.append(data)

result = 0
for i in result_zip:
  result = result + i


print(result)
