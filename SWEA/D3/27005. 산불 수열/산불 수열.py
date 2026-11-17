def solve():
    max_n = 1000
    A = [0] * (max_n +1)

    A[0] = 1
    A[1] = 1

    for i in range(2, max_n +1):
        val = 1
        while True:
            for k in range(1, (i//2)+1):
                if (val - A[i-k])==(A[i-k] - A[i-2 *k]):
                    break
            else:
                A[i] = val
                break

            val += 1
    return A

precomputed_A = solve()

TC = int(input())
for _ in range(TC):
    n = int(input())
    print(precomputed_A[n])