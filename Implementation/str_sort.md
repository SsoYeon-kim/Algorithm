알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어집니다.   
이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.   
예를 들어 K1KA5CB7이라는 값이 들어오면 ABCKK13을 출력합니다.   
   
#### 풀이   
   
1. 문자열이 입력되었을 때 문자를 하나씩 확인
2. 숫자인 경우 따로 합계를 계산
3. 알파벳인 경우 별도의 리스트에 저장
4. 리스트에 저장된 알파벳을 정렬해 출력하고, 합계를 뒤에 붙여 출력

   
<pre><code>data = input()
result = []
sum = 0

#문자를 하나씩 확인하며
for i in data:
  #알파벳인 경우 결과 리스트에 삽입
  if i.isalpha():
    result.append(i)
  #숫자는 따로 더하기
  else:
    sum += int(i)

#알파벳을 오름차순으로 정렬
result.sort()

#숫자가 존재할 경우 뒤에 삽입
if sum != 0:
  result.append(str(sum))

#리스트를 문자열로 변환하여 출력
#공백없이 리스트에 포함된 모든 문자열을 나열해서 출력
print(''.join(result))</code></pre>
   
   
'구분자'.join(리스트)
: join함수는 매개변수로 들어온 리스트에 있는 요소 하나하나를 합쳐서 문자열로 바꾸어 반환하는 함수   
   
예를들어 '_'.join(['a','b','c'])이면 "a_b_c"와 같은 형태로 문자열을 만들어서 
