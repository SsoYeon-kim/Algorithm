#n,k를 공백을 기준으로 구분하여 입력 받기
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
print(result)  
