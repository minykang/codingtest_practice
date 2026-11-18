TC = int(input())

for test_case in range(1, TC+1):
    N = int(input())
    if N % 2 == 0:
        print(f"#{test_case} Alice")
    else:
        print(f"#{test_case} Bob")