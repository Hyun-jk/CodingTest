# 피보나치 함수
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)


print(fibo(4))
#메모이제이션 기법 = 값을 저장한느 방법으로 캐싱이라고도 한다.
# 피보나치 수열 메모이제이션 기법

#한 번 계산된 결과를 메모이제이션(Memoization)하기 위한 리스트 초기화
d = [0] * 100

#피보나치 함수(Fibonaci Function)를 재귀함수로 구현(탑다운 다이나믹 프로그래밍)
def fibo(x):
    #종료 조건(1 혹은 2일 때 1을 반환)
    if x == 1 or x == 2:
        return 1
    #이미 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]
print(fibo(99))

""""
다이나믹 프로그램이란 
큰 문제를 작게 나누고, 같은 문제라면 한 번씩만 풀어 문제를 효율적으로 
해결하는 알고리즘 기법이다.
큰 문제를 작게 나누는 방법은 퀵 정렬에서도 소개된 적이 있는데
퀵 정렬은 정렬을 수행할 때 정렬할 리스트를 분할하며 전체적으로 정렬이 될 수 있도록 한다
이를 분할 정복(Divide and conquer)알고리즘으로 분류한다
다이나믹 프로그램과 분할 정복의 차이점은 다이나믹 프로그래밍은 문제들이 서로 영향을 미치고 있다는 점이다.

퀵 정렬을 예로 들면, 한 번 기준 원소(Pivot)가 자리를 변경해서 자리를 잡게 되면 그 기준 원소의 위치는
더 이상 바뀌지 않고 그 피벗값을 다시 처리하는 부분 문제는 존재하지 않는다
반면 다이나믹 프로그래밍은 한 번 해결했던 문제를 다시금 해결한다는 점이 특징이다.
그렇기 때문에 이미 해결된 부분 문제에 대한 답을 저장해 놓고, 이 문제는 이미 해결이 됐던 것이니깐 다시 해결할 필요가 없다고 반환하는 것이다.

재귀 함수를 사용하면서 컴퓨터 시스템에서는 함수를 다시 호출했을 때 메모리 상에 적재되는 일련의 과정을 따라야 하므로
오버헤드가 발생할 수 있다.
>>>반복문을 이요한 다이나믹 프로그램이 더 성능이 좋기 때문에 재귀함수 대신 반복문을 사용해서 오버헤드를 줄일 수 있다.
"""

#호출되는 함수 확인을 위한 코드
d =[0] * 100

def pibo(x):
    print('f(' + str(x)+ ')', end=' ')
    if x ==1 or x ==2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = pibo(x - 1) + pibo(x -2 )
    return d[x]

pibo(6)

#피보나치 수열 소스코드(반복적)
#앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

#첫 번째 피보나치 수와 두 번째 피보나치 수는 1
d[1] =1
d[2] =1
n = 99

#피보나치 함수를 반복문으로 구현(보텀업 다이나믹 프로그램)
for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])

#탑다운(메모이제이션) 방식은 '하향식'이라고도 하고, 보텀업 방식은 '상향식'이라고 한다.
#다이나믹 프로그래밍의 전형적인 형태는 '보텀업 방식이다.'
#보텀업 방식에서 사용되는 결과 저장용 리스트는 'DP 테이블'이라고 부르며, 메모이제이션은 탑다운 방식에 국한되어 사용되는 표현이다.
#다이나믹 프로그램맹과 메모이제이션의 개념와는 다른 개념이다.
#메모이제이션은 이전에 계산된 결과를 일시적으로 기록해 놓는 넓은 개념을 의미한다.
#한 번 계산된 결과를 어딘가에 담아 놓기만 하고 다이나믹 프로그래밍을 위해 활용하지 않을 수도 있다.













