def solution(s):
    answer = len(s)
    
    
    for k in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:k]
        cnt = 1
        for i in range(k,len(s),k):
            cur = s[i:i+k]
            if cur == prev:
                cnt +=1
            else:
                compressed += (str(cnt) if cnt > 1 else "") + prev
                prev = cur
                cnt = 1
        compressed += (str(cnt) if cnt > 1 else "") + prev
        answer = min(answer, len(compressed))
        
    return answer
