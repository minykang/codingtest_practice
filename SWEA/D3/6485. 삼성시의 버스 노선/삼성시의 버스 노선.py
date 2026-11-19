T = int(input())

for test_case in range(1,T+1):
    cnt = [0] * 5001
    N = int(input())
    for i in range(N):
        a,b = map(int,input().split())
        for k in range(a,b+1):
            cnt[k] +=1

    P = int(input())
    ans=[]
    for j in range(P):
        c = int(input())
        ans.append(str(cnt[c]))

    print(f"#{test_case} {' '.join(ans)}")
    