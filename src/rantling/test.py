import os

if __name__ == '__main__':
    print('        WELCOM        ')
    command = input('>>py:')

    while command != 'quit':
        print('>>py: This is a "%s" command' % command)
        command = input('>>py:')
    
    print('>>py: Thx for using')
    