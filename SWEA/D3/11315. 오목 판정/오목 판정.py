T = int(input())

for test_case in range(1,T+1):
    N = int(input())

    board = [input() for _ in range(N)]
    
#가로 세로 우하향 우상향
    dr = [0,1,1,-1]
    dc = [1,0,1,1]

    result = False

    for r in range(N):
        if result:
            break
        for c in range(N):
            if result:
                break

            if board[r][c] == 'o':
                for i in range(4):
                    cnt = 1

                    for step in range(1,5):
                        next_r = r + dr[i] * step
                        next_c = c + dc[i] * step

                        if (
                            0 <=next_r<N
                            and 0<= next_c < N
                            and board[next_r][next_c] =='o'
                        ):
                            cnt +=1
                        else:
                            break

                    if cnt >= 5:
                        result = True
                        break
    if result:
        print(f"#{test_case} YES")

    else:
        print(f"#{test_case} NO")