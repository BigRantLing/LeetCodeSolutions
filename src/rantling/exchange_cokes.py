def exchange_cokes(empty_bottles: int):
    if empty_bottles == 2:
        return 1
    if empty_bottles < 2:
        return 0
    
    cokes = empty_bottles // 3
    cokes += exchange_cokes(empty_bottles % 3 + cokes)
    
    return cokes


if __name__ == '__main__':
    input_list = []
    user_input = int(input())
    
    while user_input != 0:
        input_list.append(user_input)
        user_input = int(input())
    
    for empty_bottles in input_list:
        print(exchange_cokes(empty_bottles))