# 네오는 유저의 아이디 생성


def solution(new_id):
    answer = ''
    # 1단계 구현 대문자를 모두 소문자로
    new_id = new_id.lower()
    
    for ch in new_id:
        if ch.isalnum() or ch in ['-', '_', '.']:
            answer += ch
        
    while '..' in answer:
        answer = answer.replace('..','.')
    
    answer = answer.strip('.')
            
    if not answer:
        answer = "a"
    
    if len(answer) >= 16:
        answer = answer[:15].rstrip('.')
        
    while len(answer) < 3:
        answer += answer[-1]
        
    return answer