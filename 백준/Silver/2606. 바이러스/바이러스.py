# 그래프 문제
# 이게 그래프 문제인거는 알겠는데 그냥 배열 정해놓고
# 걸리면 1 아니면 0으로 하는 뭔가 감염 배열 만들어놔
# d = [] d[1] = 1 이야 무조건
# 만약 1이랑 연결되어있는거는 무조건 1이 되겠다 그리고 그러면 연결되어있는것을 보면 그 d가 1인지 아닌지 보고 0이면 넘어가고 1이면 감염이라 1로 바꿀때마다 cnt +=1 하면 될거같은데

n = int(input())
roop = int(input())
graph = [[] for _ in range(n+1)]
d = [0] * (n + 1) 
d[1] = 1
cnt = 0

def dfs(x):
    d[x] = 1 # 방문여부
    for y in graph[x]:
        if d[y] == 0:
            dfs(y)

for i in range(roop):
    a,b = map(int,input().split())
    #여기서 조건 분기
    graph[a].append(b)
    graph[b].append(a)

dfs(1)

print(sum(d)-1)