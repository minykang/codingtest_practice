# 규칙을 이해해보자면
'''
1. 공백을 기준으로 단어로 하고 뒤집는건 단어만 한다
2. 태그는 단어가 아님

'''
word = input()
in_tag =False
temp = "" # 뒤집을 배열
for ch in word:
    if ch == "<":
        in_tag =True
        print(temp[::-1], end="")
        temp = ""
        print("<",  end="")
    elif ch == ">":
        print(">",  end="")
        in_tag = False
    elif in_tag:
        print(ch, end="")
    elif ch == ' ':
        print(temp[::-1], end="")
        temp = ""
        print(" ", end="")
    else:
        temp += ch
print(temp[::-1], end = "")