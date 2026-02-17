# 일단 n이 주어지면 n*n크기의 보드를 만들자
# 보드를 만들고 나서는 그 행을 하나하나 내려가면서 좌우상하를 제외한 곳에
# 퀸을 넣을수 있다고 수를 더하자

n = int(input())

cols = [False] * n
diag1 = [False] * (2*n -1)
# 차의 대각선인 왼쪽 위를 보는 방향
diag2 = [False] * (2*n -1)
# 합의 대각선 오른쪽방향 위를 보는 것
def dfs(row):
    if row == n:
        return 1
    total = 0
    

    for col in range(n):
        d1 = row - col + n-1
        d2 = row + col
        
        if cols[col] or diag1[d1] or diag2[d2]:
            continue
        # 그 처음 행에서 열에 두었다 -> true로 바꾸기
        cols[col] = diag1[d1] = diag2[d2] = True
        total += dfs(row+1)
        # 거짓으로 돌려놓고 다음 열을 보기
        cols[col] = diag1[d1] = diag2[d2] = False

    return total

print(dfs(0))
