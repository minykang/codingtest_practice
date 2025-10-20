def solution(files):
    #일단 문자열을 파일로 입력받고 그걸 헤드 넘버 테일로 나눈다 비교의 시작은 헤드부터 비교를 하는건데 헤드와 
    #넘버의 기준은 숫자가 나오면 그걸 넘버라고 하면 되는듯
    comp = []
    for s in files:
        
        #숫자 시작 위치 찾기
        i = 0
        #여기서 s는 요소
        while i < len(s) and not s[i].isdigit():
            i += 1
        j = i
        while j < len(s) and s[j].isdigit() and (j-i) < 5:
            j += 1
        head = s[:i]
        number = s[i:j]
        
        comp.append((head.lower(), int(number), s))
    
    comp.sort(key = lambda x: (x[0], x[1]))
    return [x[2] for x in comp]
        
    
    #이렇게하면 i부터 j 까지 숫자라는거임
    
    #숫자 종료 위치 찾기
    