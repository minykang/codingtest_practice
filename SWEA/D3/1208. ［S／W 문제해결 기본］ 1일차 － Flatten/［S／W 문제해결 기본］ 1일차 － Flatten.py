T = 10

for test_case in range(1, T+1):
    dump = int(input())
    height = list(map(int,input().split()))

    for i in range(dump):
        high , low = height.index(max(height)), height.index(min(height))
        height[high] -= 1
        height[low] += 1

    result = max(height) - min(height)
    print(f"#{test_case} {result}")