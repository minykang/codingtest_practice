def solution(s):
    

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    # 그니까 스택을 만들어놓고 거기에 하나씩 넣으면서 그 새로 들어오는 거 그게 [-1]에 있는거고 그걸 기존꺼랑 비교하면서 같으면 기존꺼랑 새로 들어온 거랑 둘다 빼는거 아닌가이때 비교한는 기존은 새로 들어온 것의 앞에 꺼고
    
    stack = []
    
    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)
    if not stack:
        answer = 1
    else :
        answer = 0
    return answer