n = int(input())

num_list = list(map(int,input().split()))

max_num = max(num_list)


new_list = [(x/max_num)*100 for x in num_list]

print(sum(new_list)/n)
