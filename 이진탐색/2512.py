import sys

n = int(sys.stdin.readline())
moneys = list(map(int, sys.stdin.readline().split()))

max_money = int(sys.stdin.readline())

start = 0
end = max(moneys)

result = []

while start <= end:
  total = 0
  mid = (start + end) // 2
  for money in moneys:
    if mid < money:
      total += mid
    else:
      total += money
  if total > max_money:
    end = mid - 1
  else:
    result = mid
    start = mid + 1

print(result)
