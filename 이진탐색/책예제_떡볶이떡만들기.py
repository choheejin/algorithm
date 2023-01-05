n, m = list(map(int, input().split()))  
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0

while start <= end:
  total = 0
  mid = (start + end) // 2
  for x in array:
    if x > mid:
      total += x - mid

  # 떡의 양이 부족함 -> 더 많이 잘라야 한다.
  if total < m:
    end = mid - 1
  else:
    result = mid # 최대한 덜 잘랐을 때가 정답이므로 일단 기록
    start = mid + 1
    
print(result)
