def solution(s):
    a = 0
    b = 0
    for i in range(len(s)):
        if s[i] == 'p' or s[i] == 'P':
            a += 1
        elif s[i] == 'y' or s[i] == 'Y':
            b += 1
    
    return a == b