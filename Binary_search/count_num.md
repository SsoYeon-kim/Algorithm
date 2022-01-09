N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있습니다.   
이때 이 수열에서 x가 등장하는 횟수를 계산하세요.   
   
예를 들어 수열 {1, 1, 2, 2, 2, 2, 3}이 있을 때 x = 2라면, 현재 수열에서 값이 2인 원소가 4개이므로 4를 출력   
단, 이 문제는 시간 복잡고 O(logN)으로 알고리즘을 설계하지 않으면 시간 초과 판정을 받습니다.   
   
#### 풀이   
   
- 시간 복잡도 O(logN)으로 동작하는 알고리즘을 요구
  - 일반적인 선형 탐색으로는 시간 초과 판정
  - 하지만 데이터가 정렬되어 있기 때문에 이진 탐색을 수행할 수 있음
- 특정 값이 등장하는 첫 번째 위치와 마지막 위치를 찾아 위치 차이를 계산해 문제를 해결할 수 있음
   
    
<pre><code>from bisect import bisect_left, bisect_right

def count_by_range(array, left_value, right_value):
  right_index = bisect_right(array, right_value)
  left_index = bisect_left(array, left_value)
  return right_index - left_index

#데이터 개수 N, 찾고자 하는 값 X 입력 받기
n, x = map(int, input().split())
array = list(map(int, input().split())) #전체 데이터 입력

#값이 [x, x]범위에 있는 데이터의 개수 계산
count = count_by_range(array, x, x)

#값이 x인 원소가 존재하지 않는다면
if count == 0:
  print(-1)
else:
  print(count)</code></pre>
