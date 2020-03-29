
students_grade = []

while True:
    try:
        line_1 = input().split()
        operation_ammount = int(line_1[1])
        greades = input().split()

        for greade in greades:
            students_grade.append(int(greade))
        for i in range(0, operation_ammount):
            operations = input().split()
            command = operations[0]
            start = int(operations[1])
            end = int(operations[2])

            if command == 'Q':
                if end >= start:
                    print(max(students_grade[start - 1: end]))
                else:
                    print(max(max(students_grade[:end]), max(students_grade[start - 1:])))
            else:
                students_grade[start - 1] = end
    except:
        break
