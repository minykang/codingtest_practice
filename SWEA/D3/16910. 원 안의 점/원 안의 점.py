# *4+1로 가능하지 않을까 1 사분면만 구해도
# 반지름 주면 

T = int(input())


for test_case in range(1,T+1):
    N = int(input())
    cnt = 0
    on_line = N * 4
    for x in range(1,N+1):
        for y in range(1,N+1):
            if x*x + y*y <= N*N:
                cnt +=1
            else:
                break
    cnt = cnt * 4 +1
    result = cnt + on_line
    print(f"#{test_case} {result}")