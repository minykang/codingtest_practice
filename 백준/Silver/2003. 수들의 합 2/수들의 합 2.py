import sys
input = sys.stdin.readline
# 연속된 숫자를 더하는것 
# 잘라서 숫자를 더하면서 그 숫자가 되어야함
# 그리고 카운트를 설정해서 숫자 세기 
n,m = map(int,input().split())
num= list(map(int,input().split()))
cnt = 0
left = 0
total = 0
for right in range(n):
    total += num[right]
    while total > m:
        total -= num[left]
        left += 1
    if total == m:
        cnt +=1
print(cnt)