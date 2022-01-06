어떠한 수 N이 1이 될 때까지 다음의 과정 중 하나를 반복적으로 선택하여 수행하려고 합니다.   
단, 두 번째 연산은 N이 K로 나누어 떨어질 때만 선택할 수 있습니다.   
   
1. N에서 1을 뺍니다.
2. N을 K로 나눕니다.
N과 K가 주어질 때 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구하는 프로그램을 작성하세요.   
   
#### 방법 1   
<pre><code>#n,k를 공백을 기준으로 구분하여 입력 받기
n,k = map(int, input().split())

#연산 수행 횟수
result = 0

while True:
  #n이 k로 나누어 떨어지는 수가 될 때까지 빼기
  #n이 k로 나누어 떨어지지 않을 때 k를 곱해서 k로 나누어 떨어지는 가장 가까운 수를 찾음
  target = (n // k) * k
  #1을 빼는 횟수
  result += (n - target)
  n = target

  #n이 k보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
  if n < k:
    break

  #작지 않으면 k로 나눠주고 연산 횟수도 +1
  result += 1
  n //= k 

#마지막으로 남은 수 에 대하여 1씩 빼기
result += (n-1)
print(result)</code></pre>
   
#### 방법 2   
<pre><code>#n,k를 공백을 기준으로 구분하여 입력 받기
n,k = map(int, input().split())

count = 0

while n != 1:
  if n >= k:
    if n % k == 0:
      n //= k
      count += 1
    else:
      count += (n % k)
      n -= (n % k)
  else:
    n -= 1
    count += 1

print(count)</code></pre>
