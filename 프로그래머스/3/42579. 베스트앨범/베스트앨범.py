def solution(genres, plays):
    
    songs = {}# 노래에서는 몇번째인지랑 그 재생횟수가 리스트로 들어가야함
    total = {}# 합계에서는 횟수만 담아서 더할 수 있게 해야함
    
    for i in range(len(genres)):
        g = genres[i]
        p = plays[i]
        
        total[g] = total.get(g,0) + p
        songs[g] = songs.get(g,[]) + [(p,i)]
    
    #총 합계 내림차순으로 먼저 sort
    g_order = sorted(total.items(), key = lambda x:x[1], reverse = True)
    #이때 total.items()를 쓰게 되면 키,값 묶음이 되어 정렬이 같이 둘다 된다.    
    answer = []
    #이제 g_order에는 그럼 합계가 많은 순으로 장르가 정렬되어있기 때문에 거기에서 이제 플레이 내림차순과 고유 숫자는 오름차순으로 정렬해야한다
    for g, sum_play in g_order:
        songs[g].sort(key = lambda x:(-x[0],x[1]))
        answer += [idx for play,idx in songs[g][:2]]
        #최대 두개까지니까 고유 번호인 인덱스를 송의 배열에서 빼와서 정잡에 더해놓는다.
            
    
    return answer