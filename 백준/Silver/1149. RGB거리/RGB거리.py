# 코드를 작성해주세요
# 이 문제는 조건이 되게 많은거 같지만 전체에서 조건 하나하나를 보기 보다는 i일때 조건들을 지정
n = int(input())

cost = [list(map(int,input().split())) for _ in range(n)]

dp = [[0] * 3 for _ in range(n)]

#초기화
dp[0][0] = cost[0][0]
dp[0][1] = cost[0][1]
dp[0][2] = cost[0][2]

for i in range(1, n):
    #i의 집에서 각 색깔 골랐을때 경우의수
    dp[i][0] = cost[i][0] + min(dp[i-1][1],dp[i-1][2])  
    dp[i][1] = cost[i][1] + min(dp[i-1][0],dp[i-1][2])  
    dp[i][2] = cost[i][2] + min(dp[i-1][0],dp[i-1][1])  
    
print(min(dp[n-1][0], dp[n-1][1], dp[n-1][2]))