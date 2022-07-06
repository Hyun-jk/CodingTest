# 순차 탐색
"""
순차탐색)
- 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로
  확인하는 방법
- 보통 정렬되지 않은 리스트에서 데이터를 찾아야 할 때 사용한다.
- 순차 탐색은 이름처럼 순차로 데이터를 탐색한다는 의미
- 리스트의 데이터에 하나씩 방문하며 특정한 문자열과 같은지 검사하므로 구현도 간단
- 리스트에 특정 값의 원소가 있는지 체크할 때도 순차 탐색으로 원소를 확인하고
= 리스트 자료형에서 특정한 값을 가지는 원소의 개수를 세는 count()메서드를 이용할 때도 사용
"""

# 간단한 순차 탐색 소스코드


def sequential_search(n, target, array):
    # 각 원소를 하나씩 확인하며
    for i in range(n):
        # 현재의 원소가 찾고자 하는 원소와 동일한 경우
        if array[i] == target:
            return i + 1  # 현재의 위치 반환(인덱스는 0부터 시작하므로 1 더하기)


print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
input_data = input().split()
n = int(input_data[0])  # 원소의 개수
target = input_data[1]  # 찾고자 하는 문자열

print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다")
array = input().split()

# 순차 탐색 수행 결과 출력
print(sequential_search(n, target, array))

# 순차 탐색의 시간 복잡도
# 데이터 정렬 여부와 상관없이 가장 앞에 있는 원소부터 하나씩 확인해야 한다는 점이 특징이다
# 따라서 데이터의 개수가 N개일 때 최대 N번의 비교 연산이 필요하므로 순차 탐색의 최악의 경우
# 시간 복잡도는 O(N)이다.