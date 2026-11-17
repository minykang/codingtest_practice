T = 10

for test_case in range(1, T+1):
    num = int(input())
    board = []
    for i in range(100):
        row = list(map(int,input().split()))
        board.append(row)
        max_value = -1
    #행
    for i in range(100):
        max_value = max(sum(board[i]),max_value)
    #열
    for i in range(100):
        value = 0
        for j in range(100):
            value += board[j][i]
            max_value = max(value,max_value)
    #오른쪽 대각
    down_diagnol = 0
    for i in range(100):
        down_diagnol += board[i][i]
        max_value = max(down_diagnol,max_value)
    #왼쪽 대각
    up_diagnol = 0
    for i in range(100):
        up_diagnol += board[99-i][i]
        max_value = max(up_diagnol,max_value)

    print(f"#{test_case} {max_value}")