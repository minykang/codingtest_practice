n,m = map(int,input().split())

count = {}
ans = 0
for _ in range(n):
    not_heard = input().strip()
    count[not_heard] = count.get(not_heard,0)+  1

for _ in range(m):
    not_seen = input().strip()
    count[not_seen] = count.get(not_seen,0)+ 1

lis1 = []

for  i in count:
    if count[i] > 1:
        ans += 1
        lis1.append(i)

lis1.sort()
print(ans)
for x in lis1:
    print(x, end = "\n")