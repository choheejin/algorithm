## 탐색
많은 양의 데이터 중에서 원하는 데이터를 찾는 과정이다.     

### DFS 알고리즘
깊이 우선 탐색이라고 부르며, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘이다.  
- 인접행렬: 2차원 배열에서 각 노드가 연결된 형태를 기록하는 방식
  - 연결되지 않은 노드 끼리는 무한
  - 자기 자신은 0
 ``` python
 INF = 999999999
 
 graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
 ]
 
 print(graph)
 ```

- 인접리스트: 리스트로 그래프의 연결관계를 표현하는 방식
  - 연결리스트 사용한다
``` python
# 행이 3개인 2차원 리스트로 인접리스트 표현
graph = [[] for _ in range(3)]

# (연결된 노드, 거리)
graph[0].append((1, 7))
graph[0].append((2, 5))

graph[1].append((0, 7))

graph[2].append((0, 5))

print(graph)
```

### DFS 알고리즘 동작 과정 (stack 이용)
1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면, 그 인접 노드를 스택에 넣고 방문 처리를 한다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
3. 2번의 과정을 더이상 수행할 수 없을 때까지 반복한다
> 방문 처리는 스택에 한번 삽입되어 처리된 노드가 다시 삽입되지 않도록 체크하는 것을 의미한다. 방문 처리를 함으로써, 각 노드를 한 번씩만 처리할 수 있다.

``` python
def dfs(graph, v, visited):
  visited[v] = True
  print(v, end=" ")
  for i in graph[v]:
    if not visisted[i]:
      dfs(graph, i, visited)
      
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

dfs(graph, 1, vistied)
```

### BFS
너비 우선 탐색으로, 가까운 노드부터 탐색하는 알고리즘이다.

### BFS 동작 방식 (큐 이용)
1. 탐색 시작 노드를 큐에 삽입하고, 방문 처리를 한다.
2. 큐에서 노드를 꺼내, 해당 노드의 인접 노드 중에서 방문 하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다.
3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.
> 일반적으로, 실행 수행 시간은 DFS 보다 좋은 편이다.

``` python
from collections import deque

def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True
  while queue:
    v = queue.popleft()
    print(v, end=" ")
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)
```
