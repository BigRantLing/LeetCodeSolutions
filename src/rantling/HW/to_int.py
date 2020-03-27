
# 十六进制转十进制
num_dict = {
    'A': '10',
    'B': '11',
    'C': '12',
    'D': '13',
    'E': '14',
    'F': '15'
}


def to_int(hex_str: str):
    hex_str = hex_str.upper()
    int_list = []

    for char in hex_str:
        if char == '0' or char == 'X':
            continue

        if char in num_dict.keys():
            int_char = num_dict.get(char)
        else:
            int_char = char

        int_list.append(int_char)

    pos = len(int_list)
    result = 0

    for i in range(0, pos):
        result += int(int_list[i]) * (16**(pos-1-i))

    return result


if __name__ == '__main__':
    user_input = str(input())

    while user_input != '0':
        print(to_int(user_input))
        print()
        user_input = str(input())
