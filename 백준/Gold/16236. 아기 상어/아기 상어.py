from collections import deque

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]

visited = [0]*(n+1)

dx = [-1,1,0,0]
dy = [0,0,-1,1]
INF = int(1e9)


size = 2
sx,sy=0,0 # 현재 상어 위치

for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            sx,sy = i,j
            board[i][j] = 0 # 상어 좌표 저장했으니 이제 0으로 하기

def bfs():
    queue = deque([(sx,sy)])
    visited = [[-1] * n for _ in range(n)]
    visited[sx][sy] = 0 #이거는 아까 아기상어 위치인데 출발점이라 0

    while queue:
        x,y = queue.popleft() # x,y는 모든 탐색 후보 여기에서는 시작점이니까 상어 위치

        for i in range(4):
            nx,ny = x + dx[i], y + dy[i]

            if (0 <= nx<n) and (0 <= ny < n):
                if size >= board[nx][ny] and visited[nx][ny] == -1: #상어 위치에서 인접 네칸이고 그게 방문이 안됐다면
                    visited[nx][ny] = visited[x][y] + 1 # 방문 여부는 0+1 인 1로 한다 상어의 인접 네칸을
                    queue.append((nx,ny)) #방문을 했으니까 큐에 집어넣는다
    return visited

def find(visited):
    x,y = 0,0
    min_distance = INF

    #전체 다 돌면서 확인
    for i in range(n):
        for j in range(n):
            if visited[i][j] != -1 and 1 <= board[i][j] < size:
                if visited[i][j] < min_distance:
                    min_distance = visited[i][j]
                    x,y = i,j

    if min_distance == INF:
        return False
    else:
        return x,y, min_distance
    

ans = 0
food = 0

while True:
    result = find(bfs())

    if result == 0:
        print(ans)
        break
    else:
        
        x, y, d = result
        sx, sy = x, y
        ans += d
        board[x][y] = 0 #상어가 먹고 치운 물고기를 없애야함
        food +=1

        if food >= size:
            size += 1
            food = 0
# 결국 출력하는건  ans 인데 이게 결과가 0이 될때니까 이건 false가 나와 주변이 무한대로 아무것도 먹을게 없을때라는거임
