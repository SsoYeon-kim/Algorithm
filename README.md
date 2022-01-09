# Algorithm
Algorithm with Python   
   
1. 그리디
2. 구현 (시뮬레이션과 완전 탐색)
3. 그래프 탐색 알고리즘 (DFS/BFS)   
4. 정렬
5. 이진 탐색
6. 다이나믹 프로그래밍
7. 최단 경로 알고리즘
8. 기타 그래프 이론
9. 기타 알고리즘
   
<hr>
   
### 그리디(탐욕법)   
   
현재 상황에서 지금 당장 좋은 것만 고르는 방법   
   
<예시>   
- 거스름돈   
- 1이 될 때까지
- 곱하기 혹은 더하기
- 모험가 길드   
   
### 구현   
   
머릿속에 있는 알고리즘을 소스코드로 바꾸는 과정   
일반적으로 알고리즘 문제에서의 2차원 공간을 행렬(matrix)의 의미로 사용   
시뮬레이션 및 완전 탐색 문제에서는 2차원 공간에서의 방향 벡터가 자주 활용   
   
<pre><code>#동, 북, 서, 남
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

#현재 위치
x, y = 2, 2

for i in range(4):
  #다음 위치
  nx = x + dx[i]
  ny = y + dy[i]
  print(nx, ny)</code></pre>   
   
<예시>   
- 상하좌우
- 시각
- 왕실의 나이트
- 문자열 재정렬
   
### 그래프 탐색 알고리즘   
   
탐색 : 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정   
   
대표적인 그래프 탐색 알고리즘 : DFS, BFS   
   
* 스택 : LIFO
   * 파이썬에서는 list로 구현 (별도 라이브러리 필요 X)   
   * append로 삽입, pop으로 삭제   
   
- 큐 : FIFO
   - 파이썬에서는 deque라이브러리를 사용 (list를 이용하는 것이 시간 복잡도 더 증가)      
   - 최상단 원소부터 출력 (나가고자 하는 원소부터) => [::-1]   
   - 최하단 원소부터 출력 (오래된 것부터)
   
   - append로 삽입, popleft로 삭제   
   - queue.reverse()를 통해 출력   
 <pre><code>from collections import deque</code></pre>   

   
- 재귀함수(Recursive Function)   
문제 풀이에 사용할 때는 종료조건을 반드시 명시해야 함(함수 시작 부분에 명시)   
   
ex ) 팩토리얼, 최대공약수(GCD)_유클리드 호제법   
   
- ### DFS : 깊이 우선 탐색   
   
   - 스택 또는 재귀 함수를 사용   
   - 가장 깊은 부분을 우선적으로 탐색하고 스택에서 꺼냄   
   
1. 탐색 시작 노드를 스택에 삽입하고 방문 처리
2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 (보통 번호가 낮은 인접 노드 부터라는 조건)
3. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냄
4. 더 이상 2-3번의 과정을 수행할 수 없을 때까지 반복
   
파이썬에서는 그래프를 표현하기 위해 2차원 리스트를 사용   
   
<pre><code>def dfs(graph, v, visited):
  #현재 노드를 방문 처리
  visited[v] = True
  print(v, end=' ')
  #현재 노드와 연결된 다른 노드를 재귀적으로 방문
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

graph = [
  [], #일반적으로 노드번호 1번부터 시작, 인덱스 0은 비워둠
  [2, 3, 8],  #1번노드와 연결된 것은 2, 3, 8
  [1, 7], #2번 노드와 연결된 것은 1, 7
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

#각 노드가 방문된 정보를 표현 (1차원 리스트)
#기본값을 False로 방문하지 않은 것으로 표현
#1~8번 노드를 갖고 있기에 인덱스 0은 사용하지 않기 위해 하나 더 큰 크기로 리스트 초기화
visited = [False] * 9

dfs(graph, 1, visited)</code></pre>   
   
- ### BFS : 너비 우선 탐색   
   
   - 그래프에서 가까운 노드부터 우선적으로 탐색   
   - 큐를 이용   
   - 특정 조건에서의 최단경로에서 많이 사용   
   
1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 함
2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 *모두* 큐에 넣고 삽입하고 방문처리 함(보통 작은노드부터라는 조건)
3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복
   
<pre><code>from collections import deque

def bfs(graph, start, visited):
  #큐 구현을 위해 deque 라이브러리 사용
  queue = deque([start])
  #현재 노드를 방문 처리
  visited[start] = True
  #큐가 빌 때까지 반복
  while queue:
    #큐에서 하나의 원소를 뽑아 출력하기
    v = queue.popleft()
    print(v, end=' ')
    #아직 방문하지 않은 인접한 원소들을 큐에 삽입
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

#각 노드가 연결된 정보를 표현(2차원 리스트)
graph = [
  [],
  [2,3,8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

#각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9

bfs(graph, 1, visited)</code></pre>   
   
   
### 정렬   
   
데이터를 특정한 기준에 따라 순서대로 나열하는 것   
   
- 선택 정렬   
   - 처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸기 반복   
   
<pre><code>array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
  min_index = i #가장 작은 원소의 인덱스
  for j in range(i + 1, len(array)):
    if array[min_index] > array[j]:
     min_index = j
  array[i], array[min_index] = array[min_index], array[i] #스와핑

print(array) </code></pre>   
   
시간 복잡도는 O(N²)   
   
- 삽입 정렬   
   - 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입
   - 앞쪽의 원소는 이미 정렬되어 있다고 가정
   - 뒤쪽의 원소를 앞쪽의 원소들의 위치 중 한 곳으로 삽입 (앞쪽 원소들과 비교해 작다면 왼쪽 크다면 오른쪽)   
   
<pre><code>array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
  for j in range(i, 0, -1): #인덱스 i부터 1까지 1씩 감소하며 반복
    if array[j] < array[j - 1]:
      array[j], array[j - 1] = array[j - 1], array[j]
    else: #자기보다 작은 데이터를 만나면 그 자리에서 멈춤
      break

print(array)</code></pre>   
   
시간 복잡도는 O(N²)   
현재 리스트의 데이터가 거의 정렬되어 있는 상태라면   
최선의 경우 O(N)의 시간 복잡도를 가짐      
   
- 퀵 정렬   
   - ㅇㅇ


