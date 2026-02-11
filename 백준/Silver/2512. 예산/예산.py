'''
# 문제 푸는 순서 
    1. 먼저 문제를 제대로 이해하고 세줄? 이하 요약해보기
        - 국가 역할 요청 심사해서 돈 주기 지역마다 
        - 총액 이하에서 최대로 돈주기
        - 돈이 상한액보다 커지면 그냥 상한액으로 치환해서주고
        - 그 이하면 요청 금액으로 준다
    2. 수도코드를 작성해서 문제 풀이 큰틀 잡기
       - 수도코드 가이드:

start = 0, end = max(num_list) (최대 예산 요청값)으로 범위

while start <= end: 동안 반복합니다.

mid = (start + end) // 2 (중간값)를 정합니다.

mid로 예산을 다 더해봅니다. (total 계산)

비교하기:

만약 total <= total_money 라면?  answer = mid 라고 저장

start = mid + 1 (더 큰 쪽을 탐색)

만약 total > total_money 라면?

예산 초과 end = mid - 1 (더 작은 쪽을 탐색)
    3. 코드 작성
'''
import sys
input = sys.stdin.readline

t = int(input())

num_list = list(map(int,input().split()))
total_money = int(input())
answer = 0
start = 0
end = max(num_list)


while (start <= end):
    total = 0
    mid = (start + end) // 2
    min = 0

    for x in num_list:
        if x > mid:
            total += mid
        else:
            total += x
        
    if total <= total_money:
        answer = mid
        start = mid + 1

    else:
        end = mid -1
print(answer)