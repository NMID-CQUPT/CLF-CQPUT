Name_list = input().split(',')
Name_set = set(Name_list)
Name_list2 = list(Name_set)

# 重新排序
Name_list2.sort(key=Name_list.index)
print(Name_list2)
