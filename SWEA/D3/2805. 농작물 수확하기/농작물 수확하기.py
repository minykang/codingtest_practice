T = int(input())

for test_case in range(1,T+1):
    n = int(input())
    board = []
    for i in range(n):
        board.append(list(map(int,input())))
    m = n//2
    ans = 0
    for i in range(n):
        distance = abs(i-m) #중심으로부터 거리
        for j in range(distance, n-distance):
            ans += board[i][j]

    print(f"#{test_case} {ans}")