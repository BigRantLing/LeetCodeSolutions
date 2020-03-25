# 十进制转十六机制

hex_dict = {
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F'
}


def to_hex(num: int):
    tmp_list = []
    while num != 0:
        low_eight = num & 15
        num = num >> 4
        tmp_list.append(hex_dict.get(low_eight))

    return ''.join(reversed(tmp_list))


if __name__ == '__main__':
    user_input = int(input())

    while user_input != 0:
        print(to_hex(user_input))
        print()
        user_input = int(input())