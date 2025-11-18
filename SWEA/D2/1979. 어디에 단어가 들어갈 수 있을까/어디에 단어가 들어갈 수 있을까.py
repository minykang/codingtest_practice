t = int(input())

for tc in range(1, t+1):
    n,k = map(int,input().split())
    arr = [list(map(int, input().split()))for _ in range(n)]
    #가로와 세로 따로 보는 것이다
    answer = 0
    for r in range(n):
        cnt = 0
        for c in range(n):
            if arr[r][c] == 1:
                cnt += 1
            if arr[r][c] == 0 or c == n-1:
                if cnt == k:
                    answer += 1
                cnt = 0
    
    for c in range(n):
        cnt = 0
        for r in range(n):
            if arr[r][c] == 1:
                cnt += 1
            if arr[r][c] == 0 or r == n-1:
                if cnt == k:
                    answer += 1
                cnt = 0
    
       
    
    print(f"#{tc} {answer}")
     
