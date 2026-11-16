T = 10


for test in range(1,T+1):
    N = int(input())
    building = list(map(int,input().split()))
    cnt =0

    standard = 2

    for i in range(standard,N-standard):
        left = max(building[i-1],building[i-2])
        right = max(building[i+1],building[i+2])
        my = building[i]

        if my >left and my>right:
            best = max(left,right)
            total = my - best
            cnt+=total
        else:
            total = 0
    print(f"#{test} {cnt}")