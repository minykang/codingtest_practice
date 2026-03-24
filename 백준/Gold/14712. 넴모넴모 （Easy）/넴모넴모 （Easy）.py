import sys
input = sys.stdin.readline 
n, m = map(int, input().split()) 
visited = [([0] * m) for _ in range(n)] 
cnt = 0 
def dfs(i,j): #일단 n까지 다 가면 어떻게 놓든 끝난거니까 +1 해줘야함 
    global cnt 
    if i == n: 
        
        cnt += 1 
        return 
    ni = i 
    nj = j + 1 
    if nj == m: 
        ni = i + 1 
        nj = 0 
        # 안놓기 
    dfs(ni, nj) 
    if not (i > 0 and j > 0 and visited[i-1][j] ==1 and visited[i][j-1]==1 and visited[i-1][j-1]==1): 
        visited[i][j] = 1 
        dfs(ni,nj) 
        visited[i][j] = 0 
        # 다른 경우의수를 위해 원상 복귀 
dfs(0,0) 
print(cnt)