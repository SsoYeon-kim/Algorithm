정수 X가 주어졌을 때, 정수 X에 사용할 수 있는 연산을 다음과 같이 4가지 입니다.   
1. X가 5로 나누어 떨어지면, 5로 나눕니다. 
2. X가 3으로 나누어 떨어지면, 3으로 나눕니다.
3. X가 2로 나누어 떨어지면, 2로 나눕니다.
4. X에서 1을 뺍니다.   
   
정수 X가 주어졌을 때, 연산 4개를 적절히 사용해서 값을 1로 만들고자 합니다. 연산을 사용하는 횟수의 최솟값을 출력하세요.   
예를 들어 정수가 26이면 다음과 같이 계산해서 3번의 연산이 최솟값입니다.   
26 -> 25 -> 5 -> 1   
(1 <= X <= 30,000)   
   
#### 풀이   
   
- 최적 부분 구조와 중복되는 부분 문제를 만족
- ai = i를 1로 만들기 위한 최소 연산 횟수
- 점화식
  - ai = min(ai-1, ai/2, ai/3, ai/5) + 1
  - 단 1을 빼는 연산을 제외하고는 해당 수로 나누어떨어질 때에 한해 점화식을 적용할 수 있음
   
   
<pre<code>#정수 X를 입력 받기
x = int(input())

#앞서 계산된 결과를 저장하기 위한 DP테이블 초기화
#1의 경우에는 연산을 수행할 필요 없기 때문에 [0]으로 초기화 되어있다고 가정
d = [0] * 30001

#점화식 : ai = min(ai-1, ai/2, ai/3, ai/5) + 1
#다이나믹 프로그래밍 진행(보텀업)
for i in range(2, x + 1):
  #현재의 수에서 1을 빼는 경우
  d[i] = d[i - 1] + 1
  #현재의 수가 2로 나누어 떨어지는 경우
  if i % 2 == 0:
    d[i] = min(d[i], d[i // 2] + 1)
  #현재의 수가 3으로 나누어 떨어지는 경우
  if i % 3 == 0:
    d[i] = min(d[i], d[i // 3] + 1)
  #현재의 수가 5로 나누어 떨어지는 경우
  if i % 5 == 0:
    d[i] = min(d[i], d[i // 5] + 1)

print(d[x])</code></pre>