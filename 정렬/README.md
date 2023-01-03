# 정렬
데이터를 복잡한 기준에 따라서 순서대로 나열하는 것을 말한다.    
> 정렬 알고리즘은 이진 탐색의 전처리 과정이다.
종류 : 선택 정렬, 삽입 정렬, 퀵 정렬, 계수 정렬

## 선택 정렬
가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고, 그 다음 작은 데이터를 선택해 앞에서 두번째 데이터와 바꾸는 과정을 반복한다.   
즉, 매번 **가장 작은 것을 선택**하는 알고리즘이다.

``` python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
  min_index = i
  for j in range(i + 1, len(array)):
    if array[min_index] > array[j]:
      min_index = j
  array[i], array[min_index] = array[min_index], array[i] # swap
  
```

2중 반복문을 돌기 때문에 시간 복잡도는 O(N^2)이다.   
하지만, 특정 리스트에서 가장 작은 데이터를 찾는 일이 잦기 때문에 선택 정렬 방법은 알아둘 것!

## 삽입 정렬
데이터를 하나식 확인하며, 각 데이터를 적절한 위치에 삽입하는 방법이다.   
``` python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
  for j in range(i, 0, -1):
    if array[j] < array[j - 1]:
      array[j], array[j - 1] = array[j - 1], array[j]
    else:
      break
```
거의 정렬 된 상태의 경우, O(N)의 시간 복잡도를 가진다.

## 퀵 정렬
- 기준 데이터를 설정하고, 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방식이다.   
- 피벗이 사용된다. 피벗이란, 큰 숫자와 작은 숫자를 교환할때, 교환하기 위한 기준을 말한다. 
- 리스트에서 첫 번째 데이터를 피벗으로 정하는 호어 분할 방식이 존재한다.

### 호어분할방식의 퀵정렬
- step1 분할하기
1. 리스트에서 첫 번째 데이터를 피벗으로 설정하고 왼쪽에서부터 피벗보다 큰 데이터를 선택하고, 오른쪽에서부터 피벗보다 작은 데이터를 선택하고, 서로의 위치를 변경한다.
2. 다시 피벗보다 큰 데이터와 작은 데이터를 각각 찾는다. 찾은 뒤에는 두 값의 위치를 서로 변경한다.
3. 다시 피벗보다 큰 데이터와 작은 데이터를 찾는데, 현재 왼쪽에서부터 찾는 값과 오른쪽에서 찾는 값의 위치가 서로 엇갈리게 되면, 피벗의 위치와 작은 데이터의 위치를 서로 변경한다.
- step 2 오른쪽 정렬
- step 3 왼쪽 정렬

``` python
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
  if start >= end:
    return
  pivot = start
  left = start + 1
  right = end
  while left <= right:
    # 피벗보다 큰 데이터를 찾을 때까지 반복
    while left <= end and array[left] <= array[pivot]:
      left += 1
    while right > start and array[right] >= array[pivot]:
      right += 1
    
    if left > right: # 엇갈림
      array[right], array[pivot] = array[pivot], array[right]
    else: # 엇갈리지 않았다면, 작은 데이터와 큰 데이터를 교환한다.
      array[left], array[right] = array[right], array[left]
   
   # 분할이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
   quick_sort(array, start, right -1)
   quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
```

``` python
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
  if len(array) <= 1:
    return array
  pivot = array[0]
  tail = array[1:] # 피벗을 제외한 리스트
  
  left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
  right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분
  
  # 분할 이후 왼쪽부분과 오른쪽 부분 각각 정렬 수행
  return quick_sort(left_side) + [pivot] + quick_sort(right_side)

```

퀵 정렬의 평균 시간 복잡도는 O(NlogN)이다.


## 계수 정렬
특정한 조건이 부합할 때만 사용할 수 있지만, 매우 빠른 정렬 알고리즘이다.   
계수 정렬은 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때만 사용할 수 있다.   

``` python
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * (max(array) + 1)

for i in range(len(array)):
  count[array[i]] += 1

for i in range(len(count)):
  for j in range(count[i]):
    print(i, end=' ')

```

계수 정렬의 시간 복잡도는 O(N + K)이다.

## 코딩테스트에서의 정렬 문제 유형
1. 정렬 라이브러리로 풀 수 있는 문제
2. 정렬 알고리즘의 원리에 대해서 물어보는 문제
3. 더 빠른 정렬이 필요한 문제

