#n,k를 공백을 기준으로 구분하여 입력 받기
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

print(count)
