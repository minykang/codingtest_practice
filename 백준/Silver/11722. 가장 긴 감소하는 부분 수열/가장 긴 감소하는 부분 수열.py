# 코드를 작성해주세요
import sys
input = sys.stdin.readline


n = int(input())
arr = list(map(int,input().split()))
dp = [1] * n

# i, j일때 일단 수열에서의 크기가 앞이 더 크다면 뒤에 dp를 더하는거임
for i in range(n):
    for j in range(i):
        if arr[j] > arr[i]:
            dp[i] = max(dp[j]+1,dp[i])

ans = max(dp)
print(ans)

            
            