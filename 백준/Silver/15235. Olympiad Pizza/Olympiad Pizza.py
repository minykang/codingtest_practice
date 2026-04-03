# 배열을 순회하며 돌게 되는데 만약 거시서 조건이 달성되면 팝하면 되는거고 돌때
import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int,input().split()))
time = [0] * n
from collections import deque
q = deque()
t = 0
#(학생, 남은 피자)
for i in range(n):
    q.append((i,arr[i]))
while q:
    idx,pizza = q.popleft()
    pizza -=1
    t+=1
    if pizza == 0:
        time[idx] = t # 이거를 먼저하고 0이면 나가게 하고 0이 아닐때나 되어야 추가해줘야함 문제조건이
    else:
        q.append((idx,pizza))
    
# 큐 해서 받아야하는 피자, 남은 피자 갯수 해서 하나씩 지나갈때마다 남은거 -1 하고 이때 0되면 계속 증가 시켰던 t를 배열에 넣기

print(*time)