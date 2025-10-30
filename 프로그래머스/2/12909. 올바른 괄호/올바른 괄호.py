def solution(s):
    answer = True
    count1, count2 = 0,0
    #일단 1.)이걸로 시작하면 탈락
    #그리고 (이걸로 시작하면 분명 짝이 맞아야함 갯수가
    if s[0] == ")":
        return False
    elif s[0] != ")":
        for i in range(len(s)):
            if s[i] == "(":
                count1 += 1
            if s[i] == ")":
                count2 += 1
                if count2 > count1:
                    return False
    return count2 == count1
            