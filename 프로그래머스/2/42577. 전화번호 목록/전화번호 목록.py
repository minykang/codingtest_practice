# def solution(phone_book):
#     answer = True
#     for x in phone_book:
#         for y in phone_book:
#             if x!=y and x == y[:len(x)]:
#                 answer = False
#     return answer
# 이거는 시간초과 때문에 안됨

#startswith함수는 시작하는거를 거를 수 있는 함수

def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            answer = False
    return answer