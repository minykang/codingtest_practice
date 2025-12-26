n = int(input())

cards = list(map(int,input().split()))

m = int(input())

target = list(map(int,input().split()))

dict = {}
#이제 dict 에 nums의 숫자를 세서 있으면 더하고 없으면 1이라 해야함

for i in cards:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
#10:3,-10:1 이런식으로 저장되는거임

# 이제 그러면 dict는 개수에 따라 {3,1,...}으로 되어있음
for x in target:
    if x in dict:
        print(dict[x], end = " ")
    else:
        print(0,end=" ")



