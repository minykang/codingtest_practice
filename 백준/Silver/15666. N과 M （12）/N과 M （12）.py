import sys

input = sys.stdin.readline

n, m = map(int,input().split())

arr = list(map(int,input().split()))
a = sorted(set(arr))
path = []

def dfs(start):
    if len(path) == m:
        print(*path) # 배열 요소만 출력
        return
        
    for i in range(start,len(a)):
        path.append(a[i])
        dfs(i)
        path.pop() # 백트래킹 느낌으로 돌아가서 1,2 1,3 이런식으로 하려면 팝을 해야 이전값이 안남는다.

dfs(0)
