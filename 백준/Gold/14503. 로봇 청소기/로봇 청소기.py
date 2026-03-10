n,m = map(int,input().split())

x,y,d = map(int,input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

cnt = 0


#북동남서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

while True:
    if graph[x][y] == 0:
        graph[x][y] = 2
        cnt += 1

    moved = False #이동여부 판단 안움직임
    
    for i in range(4):
        d = (d+3) % 4
        nx = x + dx[d]
        ny = y + dy[d] # 상하좌우


        if graph[nx][ny] == 0:
            x,y = nx,ny
            moved = True
            break
            # 앞이 0이면 치워야해서 앞으로 움직여서 좌표 변경 후 
            # 움직임 여부 사실

    if not moved:
        bx = x - dx[d]
        by = y - dy[d]
        if graph[bx][by] == 1:
            break
        else:
            x,y = bx,by

print(cnt)


        