# 백준 1715번 
'''
    이건 덧셈을 할때 가장 작은 것끼리 먼저 합치고 나서
    그 합친것과 나머지를 더하는 것이 효율적
    작은것끼리 더하면 그 세숫자에서 이제 다시 알고리즘을 돌리는 구조
    재귀인가(?) 
    일단 반복되고 숫자가 하나로 이제 다 더해지면 그게 출력이 되는 것

'''
'''
힙은 완전 이진 트리 구조이며
최소 힙에서는 루트 노드가 항상 전체에서 가장 작은 값이다.
pop을 하면 마지막 노드를 루트로 올린 뒤
부모 ≤ 자식 조건을 만족할 때까지 아래로 내려가며 정렬한다.
'''
import sys
import heapq
n = int(sys.stdin.readline())
arr1 = [int(sys.stdin.readline()) for _ in range(n)]
ans = 0
heapq.heapify(arr1)

while(len(arr1)>1):
    a = heapq.heappop(arr1)
    b = heapq.heappop(arr1)
    sum = a+b
    ans += sum
    heapq.heappush(arr1,sum)


print(ans)