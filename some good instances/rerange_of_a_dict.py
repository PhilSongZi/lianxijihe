# 对字典按照相同地址分成两组。
# 简单粗暴法：复杂度o(n^2)
'''
new_dict = {}
dict1 = {'1': "a", '2': "b", '3': "a", '4': "b"}
keys = list(set(list(dict1.values())))

for new_key in keys:
    new_value = []
    for key, value2 in dict1.items():
        if value2 == new_key:
            new_value.append(key)
    new_dict[new_key] = new_value

print(new_dict)
'''


# 只遍历一次.不预先创建keys的列表，在遍历过程中判断是否已经存在，不存在就新建，存在则把值添加进列表。
dict1 = {'1': "a", '2': "b", '3': "a", '4': "b"}
dict2 = {}
for k, v in dict1.items():
    # print(k, v)
    v2 = dict2.get(v)
    if v2:
        dict2[v].append(k)
    else:
        dict2[v] = [k]
print(dict2)
