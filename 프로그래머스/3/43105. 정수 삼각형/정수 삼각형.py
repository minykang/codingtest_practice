def solution(triangle):
    
    #이럴게 초기값을 지정해줘야 dp의 시작점이 정해져서 수행가능
    dp = [[0] * len(row) for row in triangle]
    dp[0][0] = triangle[0][0]
    
    for i in range(len(triangle)-1):
        for j in range(len(triangle[i])): # len(triangle)은 삼각형의 행의 개수
            # 이때 삼각형의  -1 행 개수만큼 반복문 수행하는 이유는 범위 때문이다
            dp[i+1][j] = max(dp[i+1][j], dp[i][j]+ triangle[i+1][j])
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+ triangle[i+1][j+1])
    
    return max(dp[-1])