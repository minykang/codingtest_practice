# 코드를 작성해주세요
n = int(input())

for _ in range(n):
    k = int(input())
    cnt = 0
    visited = [False] * (k + 1)
    arr1 = [0]+ list(map(int,input().split()))

    for i in range(1,k+1):
        # 수도코드로는 일단 그럼 방문을 안하면 사이클이 되기 때문에 +1
        # 방문을 안했으면 더하고 그 
        if visited[i] == False:
            cnt += 1
            curr = i
            while not visited[curr]:
                visited[curr] = True
                curr = arr1[curr]
    print(cnt)
    
        
