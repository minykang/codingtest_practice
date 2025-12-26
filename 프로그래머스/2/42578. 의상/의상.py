def solution(clothes):
    dict = {}
    for name,kind in clothes:
        dict[kind] = dict.get(kind,0)+1
    
    answer = 1
    for kind in dict:
        answer *= (dict[kind]+1)
    
    return answer-1
#그니까 속성을 뒤에 써주는 거고 속성이 같으면 하나만 채택
#그리고 일단 하나씩 고르다가 나중에 조합인데
#속성의 문법 사용은 어케 한다?
