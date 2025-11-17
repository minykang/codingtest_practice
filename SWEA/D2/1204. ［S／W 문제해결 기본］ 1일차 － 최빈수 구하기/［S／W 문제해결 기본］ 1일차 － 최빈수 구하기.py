n = int(input())
#그니까 제일 안크면? 사는게 이득? 뒤에 비싼게 있으면 
for i in range(1,n+1):
    a = int(input())
    arr = list(map(int,input().split()))
    count = [0]* 101
    for s in arr:
        count[s] += 1

    max_score = 0
    max_cnt = 0
    for sc in range(101):
        if count[sc] >= max_cnt:
            max_cnt = count[sc]
            max_score =sc
    print(f"#{i} {max_score}")