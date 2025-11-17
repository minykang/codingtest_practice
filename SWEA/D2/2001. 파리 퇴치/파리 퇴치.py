t = int(input())

for tc in range(1,t+1):
    N,M = map(int,input().split())

    arr = [list(map(int,input().split())) for _ in range(N)]
    max_score = 0
   #이게 dx,dy로 이동하면서 해야할듯? 아니다 그냥 한 이것도 결국 맥스 카운트를 갱신하는건데 그 네칸을 난 이동하는 법이 헷갈리네
   #N-M까지만큼만 i와 j 가 이동할 수 있음 따라서 이중반복하고 그리고나서 거기서 또 이중반복 돌려서 
    for i in range(N-M+1):
        for j in range(N-M+1):
            
            full = 0
            for x in range(i,i+M):
                for y in range(j,j+M):
                    full += arr[x][y]
            
            if full >= max_score:
                max_score = full
    
    print(f"#{tc} {max_score}")
