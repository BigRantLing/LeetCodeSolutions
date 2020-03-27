import sys

students_grade = []
input_order = 1
executed_operation = 0

for line in sys.stdin:
    if line == '\n':
        break
    # Input student ammount and operation ammout
    if input_order == 1:
        operation_ammount = int(line.split()[1])
        input_order += 1

    # Initialize students grades
    elif input_order == 2:
        for grade in line.split():
            students_grade.append(int(grade))
        input_order += 1

    # Execute operations
    else:
        executed_operation += 1
        splited_line = line.split()
        operation = str(splited_line[0])
        start = int(splited_line[1])
        end = int(splited_line[2])

        if operation == 'Q':
            if end >= start:
                print(max(students_grade[start - 1: end]))
            else:
                print(max(max(students_grade[:end]), max(students_grade[start - 1:])))

        else:
            students_grade[start - 1] = end

        if executed_operation >= operation_ammount:
            break
