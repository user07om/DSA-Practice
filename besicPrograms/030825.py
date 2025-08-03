#find the smalled ele in list
list_e = [2, 4, 1, 5]
s_ele = list_e[0]
for i in range(len(list_e)):
    print(i)
    if s_ele > list_e[i]:
        s_ele = list_e[i]
print(s_ele)
