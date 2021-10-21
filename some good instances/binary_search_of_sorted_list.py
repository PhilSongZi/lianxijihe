# 问题：请编写一个二分搜索函数，搜索排序列表中的项。函数应该返回要在列表中搜索的元素的索引。
# 提示：使用 if/elif 来处理条件。
import math


def binary_search(list1, element):
    bottom = 0
    top = len(list1) - 1
    index = -1
    while top >= bottom and index == -1:
        mid = int(math.floor((top + bottom) / 2.0))
        if list1[mid] == element:
            index = mid
        elif list1[mid] > element:
            top = mid - 1
        else:
            bottom = mid + 1
    return index


li = [2, 5, 7, 9, 11, 17, 22, 222]
print(binary_search(li, 11))
print(binary_search(li, 17))
