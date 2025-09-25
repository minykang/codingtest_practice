def solution(s):
    #만약 lens가 4 또는 6 그리고 != s
    if (len(s) == 4 or len(s) == 6) and s.isdigit():
        answer = True
    else :
        answer = False
        
    return answer

