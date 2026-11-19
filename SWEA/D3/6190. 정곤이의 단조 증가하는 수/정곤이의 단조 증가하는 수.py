T = int(input())

def is_mono(n):
    s = str(n)
    for k in range(len(s) -1):
        if s[k] > s[k+1]:
            return False
    return True

for test_case in range(1,T+1):
    N = int(input())
    num = list(map(int,input().split()))

    max_num = -1

    for i in range(N):
        for j in range(i+1,N):
            prod = num[i] *num[j]

            if prod > max_num and is_mono(prod):
                max_num = prod


    print(f"#{test_case} {max_num}")