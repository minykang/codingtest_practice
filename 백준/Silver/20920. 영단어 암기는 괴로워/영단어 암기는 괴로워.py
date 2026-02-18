'''
백준 20920 문제
자주나오는 단어를 앞에 배치한다니까 Cnt 변수를 두어 개수를 세서 더 큰거 순서대로 내림차순으로 
sort 함수를 사용하여 배열에 두고 출력인데
만약 숫자가 같으면 길이가 긴거를 비교하고 길이마저 같다면 알파벳 사전 순으로 해야함
여기서 알파벳 사전 순으로 비교하는 것이 기억이 안남 이슈...
-> 세가지를 순차적으로 비교해나가는 것이기 때문에 튜플을 사용함
단어에 따른 값이 잇기 때문에 키 벨류를 사용 즉 딕셔너리 사용

-> 시간 초과 이슈로 sys 추가
'''
import sys
input = sys.stdin.readline

n,m = map(int,input().split())

d = {}

for _ in range(n):
    word = input().rstrip()
    if len(word) >= m:
        
        if word in d:
            d[word] += 1
        else:
            d[word] = 1

result = sorted(d.items(),key=lambda x: (-x[1],-len(x[0]),x[0]))

for x in result:
    print(x[0])

# 배운점
'''
튜플 문법 항상 까먹기 때문에 암기 items()는 키와 벨류 둘다 출력 키 정하고 튜플로 어떤 값을
어떻게 출력할 것인지 설정하기
'''