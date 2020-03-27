# 十进制转十六机制
"""
思路是通过将数与15进行&操作获取最低4位的值，将这个值转换成16进制
对应的结果，然后右移4位，将转换过的数值移走。然后继续操作，直到将
所有的值都转换成16进制，然后合并。
用的是2进制转16进制一样的套路，4个二进制可以表示一个16进制数字。
"""

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