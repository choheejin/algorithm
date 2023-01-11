import sys

n = int(sys.stdin.readline())

nums = [[] for _ in range(n)]

for i in range(n):
  x, y = map(int, sys.stdin.readline().split())
  nums[i] = [x, y]

nums.sort(key=lambda x:x[1])

# print(nums)

rest = []
start = 1

for i in range(0, n-1):
  gap = nums[i+1][1] - nums[i][1] + 1
  # print(start)
  if gap < nums[i+1][0]:
    end = nums[i+1][1] - nums[i+1][0]
    tmp = end - nums[i][0]
    rest.append(tmp-start)
    start = tmp + nums[i][0]
  if gap == nums[i+1][0]:
    tmp = nums[i][1] - nums[i][0]
    rest.append(tmp-start)
    start = tmp + nums[i][0]
  else:
    tmp = nums[i][1] - nums[i][0] + 1
    rest.append(tmp - start)
    start = tmp + nums[i][0]

gap = nums[i][1] - nums[i+1][1] + 1
if gap == nums[i+1][0]:
  tmp = nums[i][1] - nums[i][0]
  rest.append(tmp-start)
else:
  tmp = nums[i+1][1] - nums[i+1][0] + 1
  rest.append(tmp - start)
# print(rest)

print(max(rest))


# 구글링

import sys
input=sys.stdin.readline

n=int(input())
arr=[]
for i in range(n):
    d,t=map(int,input().split())#소요일, 마감일
    arr.append([d,t])
arr.sort(key=lambda arr:arr[1],reverse=True)#마감일 기준 내림차순 정렬

time=arr[0][1]#과제를 시작해야 하는 날

for i in range(n):
    s=arr[i][0]
    e=arr[i][1]
    
    if time>=e:#마감일이 시작일보다 이른 경우
        time=e-s
    else:#마감일이 시작일보다 늦는 경우
        time=time-s
print(time)

