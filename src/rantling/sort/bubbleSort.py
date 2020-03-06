# coding= utf-8
class bubbleSort(object):
    def __init__(self):
        pass

    def sort(self, list_to_sort: list) -> list:
        length = len(list_to_sort)
        if length == 0 or length == 1:
            return list_to_sort
        # python 的range是左闭右开
        # 外部的i记录有多少的元素排好序了
        for i in range(0, length-1):
            # 内部循环用来找出未排序元素中的最值
            # 并移动到最右端
            for j in range(0, length-1-i):
                if list_to_sort[j] > list_to_sort[j+1]:
                    # 交换位置
                    tmp = list_to_sort[j+1]
                    list_to_sort[j+1] = list_to_sort[j]
                    list_to_sort[j] = tmp

        return list_to_sort


if __name__ == '__main__':
    res = bubbleSort().sort([1, 4, 6, 7, 8, 9, 34, 45, 6, 2, 5, 76, 1])
    print(res)
