행복 왕국의 왕실 정원은 체스판과 같은 8 × 8 좌표 평면입니다.   
왕실 정원의 특정한 한 칸에 나이트가 서 있습니다. 나이트는 매우 충성스러운 신하로서 매일 무술을 연마합니다.   
나이트는 말을 타고 있기 때문에 이동을 할 때는 L자 형태로만 이동할 수 있으며 정원 밖으로는 나갈 수 없습니다.   
나이트는 특정 위치에서 다음과 같은 2가지 경우로 이동할 수 있습니다.   
- 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
- 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기

이처럼 8 × 8 좌표 평면상에서 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램을 작성하세요.   
왕실의 정원에서 행 위치를 표현할 때는 1부터 8로 표현하며,   
열 위치를 표현할 때는 a부터 h로 표현합니다.   
   
#### 풀이   
   
나이트의 8가지 경로를 하나씩 확인하며 각 위치로 이동이 가능한지 확인
- 리스트를 이용하여 8가지 방향에 대한 방향 벡터를 정의

#### 방법 1
<pre><code>#현재 나이트의 위치 입력받기
location = input()

#문자를 아스키코드로 바꾼 값 - a를 아스키코드로 바꾼 값을 빼고 + 1
#column = int(ord(location[0])) - int(ord('a')) + 1
column = int(ord(location[0])) - 96
row = int(location[1])

#나이트가 이동할 수 있는 8가지 방향 정의
#2차원 배열로 dx,dy를 사용하지 않고 하나의 리스트를 이용한 방법
steps = [(-2,1), (-1,-2), (1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,1)]

count = 0

for step in steps:
  n_row = row + step[0]
  n_cloumn = column + step[1]
  if n_row >= 1 and n_row <= 8 and n_column >= 1 and n_column <= 8:
    count += 1

print(count)</code></pre>
   
#### 방법 2   
<pre><code>#현재 나이트의 위치 입력받기
location = input()

#문자를 아스키코드로 바꾼 값 - a를 아스키코드로 바꾼 값을 빼고 + 1
#column = int(ord(location[0])) - int(ord('a')) + 1
column = int(ord(location[0])) - 96
row = int(location[1])

dx = [-2,-2,2,2,-1,-1,1,1]
dy = [-1,1,-1,1,-2,2,-,2,2]

count = 0

for i in range(8):
  n_row = row + dx[i]
  n_cloumn = column + dy[i]
  if n_row >= 1 or n_row <= 8 and n_column >= 1 and n_column <= 8:
    count += 1

print(count)</code></pre>
