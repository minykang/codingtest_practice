n = int(input())

gualho = list(input().strip() for _ in range(n))


for i in range(len(gualho)):

    cnt1,cnt2 = 0,0
    ok = True

    for j in range(len(gualho[i])):


        if gualho[i][j] == '(':
            cnt1 += 1

        elif gualho[i][j] == ')':
            cnt2 += 1

        if (cnt2 > cnt1):
            ok = False
            break
    if ok == True and cnt1 == cnt2:
        print("YES")
    else:
        print("NO")

