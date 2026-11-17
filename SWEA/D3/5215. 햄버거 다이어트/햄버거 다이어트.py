T = int(input())

for test_case in range(1,T+1):
    N,L = map(int,input().split())
    ingredients = []
    for _ in range(N):
        score,cal = map(int,input().split())
        ingredients.append((score,cal))

    dp = [0] * (L+1)

    for score,cal in ingredients:
        for w in range(L,cal -1, -1):
            dp[w] = max(dp[w],dp[w - cal] + score)

    print(f"#{test_case} {dp[L]}")