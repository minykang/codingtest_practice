
# WHILE루프를 돌려서 해결
# 방문 여부로 경우의 수를 돌려야함
import sys

input = sys.stdin.readline

n,k = map(int,input().split())
arr = list(map(int,input().split()))
visited = [False] * n
cnt = 0

def dfs(depth,cur):
    global cnt
    
    if depth == n:
        cnt+=1
        return
    for i in range(n):
        if not visited[i]:
            next = cur -k + arr[i]
            if next >= 500:
                visited[i] = True
                dfs(depth + 1,next)
                visited[i] = False

dfs(0,500)
print(cnt)
