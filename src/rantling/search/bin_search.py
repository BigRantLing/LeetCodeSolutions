# Binary search applies to ordered data
def search(data, dst):
    if dst < data[0] or dst > data[-1]:
        return None

    low = 0
    heigh = len(data) - 1
    mid = (low + heigh) // 2

    while low <= heigh:
        mid = (low + heigh) // 2

        if dst > data[mid]:
            low = mid + 1
        elif dst < data[mid]:
            heigh = mid - 1
        else:
            return mid


if __name__ == '__main__':
    data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(search(data, 10))
