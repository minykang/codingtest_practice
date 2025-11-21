#이거는 이제 최소를 골라서 뒤로 보내고
#최대를 찾아서 맨앞으로 보내야하는거같음
#근데 횟수는 뒤에 받는 숫자로
#그러면 반복문은 최대 받는 숫자 까지 하고 
#거기서 맥스 찾고 미니멈 찾아서 그 둘의 자리를 교환하면 되는거 아님??

def dfs(cnt):
    global best, nums,n, k, visited 
    # n은 전체 길이 , best는 가장 큰 숫자 조합, k는 주어진 교환 횟수, nums는 숫자 배열
    if cnt == k:
        best = max(best,int(''.join(nums)))
        return
    state = ''.join(nums)#state는 배열을 모아놓은것
    if (cnt,state) in visited:
        return
    visited.add((cnt,state))

    for i in range(n-1):
        for j in range(i+1,n):
            nums[i],nums[j] = nums[j],nums[i]
            dfs(cnt+1)
            nums[i],nums[j] = nums[j], nums[i]


t = int(input())

for tc in range(1,t+1):
    s,k = input().split()
    
    k = int(k)

    nums = list(s)
    n = len(nums)
    best = 0
    visited = set()

    dfs(0)


        
    print(f"#{tc} {best}")





