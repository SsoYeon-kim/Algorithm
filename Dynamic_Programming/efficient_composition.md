N가지 종류의 화폐가 있습니다.   
아 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록 하려고 합니다.   
이때 각 종류의 화폐는 몇 개라도 사용할 수 있습니다.   
예를 들어 2원, 3원 단위의 화폐가 있을 때는 15원을 만들기 위해 3원을 5개 사용하는 것이 가장 최소한의 화폐 개수입니다.   
M원을 만들기 위한 최소한의 화폐 개수를 출력하는 프로그램을 작성하세요.   
   
(1 <= N <= 100, 1 <= M <= 10,000)   
   
#### 풀이   
   
- ai = 금액 i를 만들 수 있는 최소한의 화폐 개수
- k = 각 화폐의 단위
- 점화식
  - 각 화폐 단위인 k를 **하나씩 확인하며**
  - ai-k 를 만드는 방법이 존재하는 경우, ai = min(ai, ai-k + 1)
    - i가 인덱스이고 k가 화폐단위 일 때, 인덱스 2는 2원 따라서 i-k원이 존재한다면 i원을 만들 수 있다는 뜻
  - ai-k를 만드는 방법이 존재하지 않는 경우, ai = INF
     
     
 <pre><code>#정수 N, M입력 받기
n, m = map(int, input().split())
#N개의 화폐 단위 정보를 입력받기
array = []
for i in range(n):
  array.append(int(input()))

#한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
#M값 최대가 10000이기 때문에 10001을 INF로 정의
#0원부터 M원까지 금액에 대한 것이므로 M+1만큼의 DP테이블
d = [10001] * (m + 1)

#다이나믹 프로그래밍 진행(보텀업)
#i : 각각의 화폐 단위
#j : 각각의 금액
d[0] = 0
for i in range(n):
  for j in range(array[i], m + 1):
    if d[j - array[i]] != 10001:  #((i - k)원을 만드는 방법이 존재하는 경우)
      d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] == 10001: #최종적으로 M원을 만드는 방법이 없는 경우
  print(-1)
else:
  print(d[m])</code></pre>
