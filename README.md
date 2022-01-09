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
   - 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
   - 가장 기본적인 퀵 정렬은 첫 번째 데이터를 기준 데이터(Pivot)으로 설정
   - 왼쪽부터 피벗보다 큰 값을 선택, 오른쪽부터 피벗보다 작은 값을 선택하고 서로 위치 변경
   - 두숫자의 위치가 *엇갈리는 경우* 피벗과 *작은 데이터(right)*의 위치를 서로 변경
      - 피벗을 기준으로 데이터 묶음을 나누는 작업을 분할(Divide)라고 함
   - 이후 왼쪽 데이터 묶음, 오른쪽 데이터 묶음에 대해 퀵 정렬 수행(재귀적으로)
   
<pre><code>array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
  if start >= end: #원소가 1개인 경우 종료
    return
  
  pivot = start #피벗은 첫 번째 원소
  left = start + 1
  right = end
  while(left <= right):
    #피벗보다 큰 데이터를 찾을 때까지 반복
    left += 1
  while(right > start and array[right] >= array[pivot]):
    right -= 1
  if(left > right): #엇갈렸다면 작은데이터와 피벗을 교체
    array[right], array[pivot] = array[pivot], array[right]
  else: #엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
    array[left], array[right] = array[right], array[left]
  #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
  quick_sort(array, start, right - 1)
  quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)</code></pre>   
   
또는   
   
<pre><code>array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
  #리스트가 하나 이하의 원소만은 담고 있다면 종료
  if len(array) <= 1:
    return array
  pivot = array[0]  #피벗은 첫 번째 원소
  tail = array[1:]  #피벗을 제외한 리스트

  left_side = [x for x in tail if x <= pivot] #분할된 왼쪽 부분
  right_side = [x for x in tail if x > pivot] #분한된 오른쪽 부분

  #분할 이후 왼쪽,오른쪽 부분에서 각각 정렬 수행하고, 전체 리스트 반환
  return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))</code></pre>
시간 복잡도는 O(NlogN)   
최악의 경우 O(N²)   
   
   
- 계수 정렬
   - 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠르게 동작하는 정렬 알고리즘
   - 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 사용 가능
   - 데이터의 개수가 N, 데이터(양수) 중 최댓값이 K일 때 최악의 경우에도 수행시간 O(N + K)를 보장
   
1. 데이터를 모두 담을 수 있는 리스트를 생성
2. 각 인덱스가 데이터의 값에 해당하게 되고 각각의 데이터가 몇 번 씩 등장했는디 개수를 count
3. 결과를 확인할 때는 리스트의 첫 번째 데이터부터 하나씩 그 값만큼 반복하며 인덱스를 출력   
   
<pre><code>#모든 원소의 값이 0보다 크거나 같다고 사정
array = [7, 5, 9, 0, 3, 2, 6, 3, 9, 1, 4, 8, 0, 5, 2]
#모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)

for i in range(len(array)):
  count[array[i]] += 1 #각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)):  #리스트에 기록된 정렬 정보 확인
  for j in range(count[i]):
    print(i, end=' ') #띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력</code></pre>   
    
시간 복잡도와 공간 복잡도 모두 O(N + K)   
때에 따라서 심각한 비효율성을 초래   
동일한 값을 가지는 데이터가 여러 개 등장할 때 효과적으로 사용   
   
### 이진 탐색   
   
- 순차 탐색 : 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인
- 이진 탐색 : *정렬되어 있는 리스트*에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색
   - 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정함
      - 시작점, 끝점, 중간점은 인덱스를 의미하고 중간점은 소수점 이하 제거한 수
- 중간점보다 작은걸 찾는 경우 끝점을 중간점의 왼쪽으로 옮김
- 중간점보다 큰걸 찾는 경우 시작점을 중간점의 오른쪽으로 옮김

<pre><code>def binary_search(array, target, start, end):
  if start > end:
    return None
  mid = (start + end) // 2
  #찾은 경우 중간점 인덱스 반환
  if array[mid] == target:
    return mid
  #중간점의 값보다 찾고하 하는 값이 작은 경우 왼쪽 확인
  elif array[mid] > target:
     return binary_search(array, target, start, mid - 1)
  #중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
  else:
    return binary_search(array, target, mid + 1, end)

#n(원소의 개수)과 target(찾고자 하는 값)을 입력 받기
n, target = list(map(int, input().split()))
#전체 원소 입력 받기
array = list(map(int, input().split()))

#이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
  print("원소가 존재하지 않습니다.")
else:
  print(result + 1 , "번째에 있습니다.")</code></pre>   
     
 또는   
    
 <pre><code>def binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    #찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
      return mid
    #중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
      end = mid - 1
    #중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
      start = mid + 1
  return None


#n(원소의 개수)과 target(찾고자 하는 값)을 입력 받기
n, target = list(map(int, input().split()))
#전체 원소 입력 받기
array = list(map(int, input().split()))

#이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
  print("원소가 존재하지 않습니다.")
else:
  print(result + 1 , "번째에 있습니다.")</pre></code>   
    
 단계마다 탐색 범위를 2로 나누는 것과 동일하기 때문에 연산횟수는 log₂N에 비례   
 시간 복잡도는 O(logN)   
    
 - 파이썬 이진 탐색 라이브러리
   - bisect_left(a, x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환 
   - bisect_right(a, x) :정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환   
    
<pre><code>from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))</code></pre>   
   

