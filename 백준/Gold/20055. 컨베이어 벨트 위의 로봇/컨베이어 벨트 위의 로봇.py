n,k = map(int,input().split())
belt = list(map(int,input().split()))
robot = [0] * n
'''
로봇이 이동할때는 역순으로 세야한다 그 이유는 로봇은 다음칸이
비어있어야 이동을 하는데 정방향으로 보면
그 다음이 비어있지 않아서 당연히 이동을 못해서 먼저 나가있는 거를 보려면 
역방향으로 배열을 봐서 로봇을 이동시켜야한다.
'''
cnt = belt.count(0) # 처음부터 0인 경우 내구도가 그걸 세야한다
step = 0
while(cnt < k):
    step += 1
    '''
    이게 벨트는 마지막이 젤 앞으로 그리고 마지막 제외한 앞을 붙이면 
    회전벨트 한번 움직인거고 
    로봇은 회전하면 처음에 새로봇 안생기니까 0이고
    그리고 마지막 전까지 붙이고 n-1은 내리는 자리니까 0이라고 한거
    '''
    belt = [belt[-1]] + belt[:-1]
    robot = [0] + robot[:-1]
    robot[n-1] = 0
    for i in range(n-2,-1,-1):
        if robot[i] == 1 and robot[i+1] == 0 and belt[i+1] >= 1:
            robot[i+1] = 1
            robot[i] = 0
            belt[i+1] -= 1
            if belt[i+1] == 0:
                cnt += 1
    robot[n-1] = 0
    #올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
    if robot[0] == 0  and belt[0] >= 1:
        robot[0] = 1
        belt[0] -= 1
        if belt[0] == 0:
            cnt += 1
    

print(step)