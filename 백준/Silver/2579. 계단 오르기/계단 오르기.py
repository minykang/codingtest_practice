import sys
input = sys.stdin.readline

# 최종 목적지로 가기 위한 경우가 두가지 있음 바로 전에서 오면 그 전은 못오고 무조건 전전을 들림

n = int(input())

arr = list(int(input()) for _ in range(n))

if n == 1:
    print(arr[0])
    sys.exit(0) ## 안넣으면 런타임 에러남 이걸넣어줘야 이거일때는 종료하는거임
if n == 2:
    print(arr[0]+arr[1])
    sys.exit(0)


dp = [0] * n

dp[0] = arr[0]
dp[1] = arr[0] + arr[1]
dp[2] = max(arr[0]+arr[2],arr[1]+arr[2])


for i in range(3,n):
    dp[i] = max(dp[i-2] + arr[i], dp[i-3] + arr[i-1]+arr[i])

print(dp[n-1])