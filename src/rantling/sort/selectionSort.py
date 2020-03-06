# coding= utf-8
class selectionSort(object):
    def __init__(self):
        pass

    def sort(self, list_to_sort: list) -> list:
        length = len(list_to_sort)
        if length == 0:
            return list_to_sort

        for i in range(0, length-1):
            min_index = i
            for j in range(i+1, length):
                # select the index of smallest element
                if list_to_sort[j] < list_to_sort[min_index]:
                    min_index = j
            # exchange the elements
            tmp = list_to_sort[i]
            list_to_sort[i] = list_to_sort[min_index]
            list_to_sort[min_index] = tmp

        return list_to_sort


if __name__ == '__main__':
    res = selectionSort().sort([1, 4, 6, 7, 8, 9, 34, 45, 6, 2, 5, 76, 1])
    print(res)
