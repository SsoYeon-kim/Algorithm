소연이는 두 개의 배열 A와 B를 가지고 있습니다.   
두 배열은 N개의 원소로 구성되어 있으며, 배열의 원소는 모두 자연수 입니다.   
소연이는 최대 K 번의 바꿔치기 연산을 수행할 수 있는데, 바꿔치기 연산이란 배열 A에 있는 원소 하나와 배열 B에 있는 원소 하나를 골라서 두 원소를 서로 바꾸는 것을 말합니다.   
소연이의 최종 목표는 배열 A의 모든 원소의 합이 최대가 되도록 하는 것입니다.   
N, K 그리고 배열 A와 B의 정보가 주어졌을 때, 최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값을 출력하는 프로그램을 작성하세요.   
   
#### 풀이   
   
매번 배열 A에서 가장 작은 원소를 골라서, 배열 B에서 가장 큰 원소와 교체   
A에 대해 오름차순 정률, B에 대해 내림차순 정렬   
이후 두 배열의 원소를 첫 번째 인덱스부터 차례로 확인하면서 A의 원소가 B의 원소보다 작을 때에만 교체를 수행   
   
<pre><code>n, k =map(int(input().split()))
array_a = list(map(int, input().split()))
array_b = list(map(int, input().split()))

array_a.sort()  #오름차순 정렬
array_b.sort(reverse=True)  #내림차순으로 정렬

#첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 k번 비교
for i in range(k):
  #A의 원소가 B의 원소보다 작은 경우
  if array_a[i] < array_b[i]:
    #두 원소를 교체
    array_a[i], array_b[i] = array_b[i], array_a[i]
  else: #A의 원소가 B의 원소보다 크거나 같을 때, 반복문을 탈출
    break

print(sum(array_a))
</code></pre>   
   
