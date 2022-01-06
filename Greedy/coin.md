거스름돈 문제   
- 큰 단위가 항상 작은 단위의 배수이므로 작은 단위의 동전들을 조합해 다른 해가 나올 수 없으므로 그리디 사용 가능

<pre><code>n = 1260
count = 0

#큰 단위의 화폐부터 차례대로 확인하기
array = [500, 100, 50, 10]

for coin in array:
  count += n // coin #해당 화폐로 거슬러 줄 수 있는 동전의 개수
  n %= coin

print(count)
</code></pre>
