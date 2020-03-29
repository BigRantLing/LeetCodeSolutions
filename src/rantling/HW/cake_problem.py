def yestoday_cakes(taday_cakes):
    return 1.5 * (taday_cakes+1)


if __name__ == '__main__':
    n = int(input().split()[0])
    cake = 1
    for day in range(0, n-1):
        yestoday_cake = yestoday_cakes(cake)
        cake = yestoday_cake
        print(cake)
    print(cake//1)
