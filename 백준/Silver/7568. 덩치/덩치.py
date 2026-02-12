# 7568 번
'''
1. 문제 이해
누가 덩치냐를 구분하는 문제
키와 몸무게 각각을 비교해서 둘 다 크면 덩치가 크다고 말함
자신보다 덩치가 큰 사람 수 +1이 자신의 덩치 등수
덩치를 세고 cnt로 카운트를 해나가는 방법을 해야한다.
'''
'''
수도코드 
먼저 전체 사람 수 입력받기
    map을 이용해서 이중리스트 받기
    몸무게 요소끼리 비교 + 키 비교 둘다 클때 그 리스트에 맞는 것의 카운트 늘리기
    각각 카운트 +1 이 자신의 덩치 등수
    [[55, 185], 
    [58, 183], 
    [88, 186], 
    [60, 175], 
    [46, 155]]
'''

n = int(input())
arr = [0] * n
weight = [list(map(int,input().split())) for _ in range(n)]

#weight[0][0]weight[1][0]

for i in range(0,n-1):
    for j in range(1,n-i):
        if weight[i][0] < weight[i+j][0] and weight[i][1] < weight[i+j][1] :
            arr[i] += 1
        elif  weight[i][0] > weight[i+j][0] and weight[i][1] > weight[i+j][1] :
            arr[i+j] += 1

for x in arr:
    print(x+1, end = " ")
