# 코드를 작성해주세요
# 하나씩, 두개씩 점점 쪼개는 문자열 슬라이싱?
word = input().strip()
s = set()
for i in range(len(word)):
    for j in range(i+1, len(word)+1):
        s.add(word[i:j])
        
print(len(s))
# 하나씩해서 그 안에 넣어
# 만약 안에 in으로 했을때 있어 그럼 안넣고
# 없으면 넣어
# 이렇게 그 문자열 총개수로 잘라보고
# 해서 넣은 것들을 문자열 cnt 한다.