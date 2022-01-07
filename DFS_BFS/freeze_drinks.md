N × M 크기의 얼음 틀이 있습니다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시됩니다.   
구멍이 뚫려 있는 부분끼리 상, 하 , 좌, 우로 붙어있는 경우 서로 연결되어 있는 것으로 간주합니다.   
이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하세요.   
   
#### 풀이   
   
DFS 혹은 BFS로 해결 가능   
상, 하, 좌, 우 로 연결되어 있다고 표현할 수 있으므로 그래프 형태로 모델링 할 수 있음   
이동가능한 모든 노드에 대해서 방문 처리   
   
#### DFS 사용   
   
1. 특정한 지점의 주변 상, 하, 좌, 우를 살펴본 뒤에 주변 지점 중에서 값이 '0'이면서 아직 방문하지 않은 지점이 있다면 해당 지점을 방문
2. 방문한 지점에서 다시 상, 하, 좌, 우를 살펴보면서 방문을 진행하는 과정을 반복하면, 연결된 모든 지점을 방문할 수 있음
3. 모든 노드에 대하여 1~2번의 과정을 반복하며, 방문하지 않은 지점의 수를 카운트
   
#### 방법 1   
   
<pre><code>#DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(x, y):
  #주어진 범위를 벗어나는 경우에는 즉시 종료
  if x<= -1 or x >= n or y <= -1 or y >= m:
    return False
  #현재 노드를 아직 방문하지 않았다면
  if graph[x][y] == 0:
    #해당 노드 방문 처리
    graph[x][y] = 1
    #상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
    dfs(x -1, y)
    dfs(x, y - 1)
    dfs(x + 1, y)
    dfs(x, y + 1)
    return True
  return False #1을 만났을 때 

#N. M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

#2차원 리스트의 맵 정보 입력 받기
graph = []

for i in range(n):
  graph.append(list(map(int, input())))

#모든 노드(위치)에 대하여 음료수 채우기
count = 0

for i in range(n):
  for j in range(m):
    if dfs(i, j) == True:
      count += 1

print(count)</code></pre>
   
#### 방법 2   
<pre><code>n, m = map(int, input().split())
ice = []

for i in range(n):
  ice.append(list(input()))

def dfs(i,j):
  if i <= -1 or i >= n or j <= -1 or j >=m:
    return False

  if ice[i][j] == '0':
    ice[i][j] = '1'
    dfs(i+1, j)
    dfs(i-1, j)
    dfs(i, j-1)
    dfs(i, j+1)
    return True
  return False

count = 0

for i in range(n):
  for j in range(m):
    if dfs(i,j):
      count += 1

print(count)</code></pre>   
   
   
   <hr>
그래프를 채울 때 int형으로 저장할 것인지 문자열로 저장할 것인지의 차이   
   
<pre><code>for i in range(n):
  graph.append(list(map(int, input())))</code></pre>
 - 공백으로 구성되어 있지 않고 0과 1로 구성된 문자열을 입력 받을 시 각 원소에 대해 int형으로 바꾼 후 리스트로 만듦

   
<pre><code>for i in range(n):
  ice.append(list(input()))</code></pre>
- 문자열로 리스트에 추가, 이후 '0' or '1'의 형식으로 
