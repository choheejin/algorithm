# 순차 탐색
- 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법이다.   
- 보통 정렬되지 않은 리스트에서 데이터를 찾아야 할 때 사용한다.
- 최악의 경우 시간 복잡도 O(N)

``` python
def sequential_search(n, target, array):
  for i in range(n):
    if array[i] == target:
      return i + 1

print("생성할 원소의 개수를 입혁한 다음 한칸 띄고 찾을 문자열을 입력하세요")
input_data = input().split()
n = int(input_data[0])
target = input_data[1]

print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다")
array = input().split()

print(sequential_search(n, target, array))
```

# 이진 탐색
- 배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있는 알고리즘
- 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터를 찾는다.
- 한번 확인할 때마다 확인하는 원소의 개수가 절반씩 줄어들기 때문에 시간복잡도는 O(logN)이다.

## 재귀 함수로 구현
``` python
def binary_search(array, target, start, end):
  if start > end:
    return None
  mid = (start + end) // 2
  if array[mid] == target:
    return mid
  elif array[mid] > target:
    return binary_search(array, target, start, mid-1)
  else:
    return binary_search(array, target, mid+1, end)

n, target = map(int, input().split())
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
  print('찾는 원소가 없습니다.')
else:
  print(result + 1)
```

## 반복문으로 구현
``` python
def binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    if array[mid] == target:
      return mid
      
    elif array[mid] > target:
      end = mid - 1
      
    else :
      start = mid + 1
  return None

n, target = map(int, input().split())
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
  print('찾는 원소가 없습니다.')
else:
  print(result + 1)
```

# 이진 탐색 트리
- 이진 탐색이 동작할 수 있도록 고안된, 효율적인 탐색이 가능한 자료구조이다. 
- 이진 트리가 가지는 특성
  - 부모노드 보다 왼쪽 자식 노드가 작다
  - 부모노드 보다 오른쪽 자식 노드가 크다
  - 왼쪽 자식 노드 < 부모노드 < 오른쪽 자식 노드

