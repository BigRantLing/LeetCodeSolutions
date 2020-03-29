while True:
    try:
        a, b = map(int, input().split())
        grades = list(map(int, input().split()))
        for i in range(b):
            command = input().split()
            if command[0] == "Q":
                start, end = sorted([int(command[1]), int(command[2])])
                print(max(grades[start - 1:end]))
            else: grades[int(command[1]) - 1] = int(command[2])
    except:
        break
