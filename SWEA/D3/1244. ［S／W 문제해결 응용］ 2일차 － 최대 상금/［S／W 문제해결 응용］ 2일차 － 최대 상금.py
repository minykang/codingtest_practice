def dfs(k):
    global max_ans

    if k ==N:
        current_val = int("".join(nums))
        if current_val > max_ans:
            max_ans = current_val
        return

    state = (k,"".join(nums))
    if state in visited:
        return
    visited.add(state)

    length = len(nums)
    for i in range(length):
        for j in range(i+1,length):
            nums[i], nums[j] = nums[j],nums[i]

            dfs(k+1)

            nums[i], nums[j] = nums[j], nums[i]

T = int(input())
for test_case in range(1, T+1):
    data,changes = input().split()
    nums = list(data)
    N = int(changes)

    max_ans=0
    visited = set()

    dfs(0)
    print(f"#{test_case} {max_ans}")