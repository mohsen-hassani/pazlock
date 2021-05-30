'''Change Data Representation

    Methods in this module changes representation of data from string 
    to int and vice versa
'''
import sys
import logging

def int_representation(str_value, zfill=3):
    '''Convert a string to it's int representation '''
    result = ''
    str_value = str(str_value)
    for ch in str_value:
        if not ch.isascii():
            raise ValueError(f'The value "{str_value} is not ascii')
        inted = ord(ch)
        stred = str(inted)
        padded = stred.zfill(zfill)
        result += padded
    return result

def str_representation(int_value, step=3):
    '''Convert a sequece of digits to str '''
    result = ''
    int_value = str(int_value)
    len_value = len(int_value)
    for i in range(0, len_value, step):
        try:
            digit = int(int_value[i: i + step])
        except ValueError:
            raise ValueError(f'The value "{int_value}" is not number')
        char = chr(digit)
        result += char
    return result

if __name__ == '__main__':
    args = sys.argv
    if len(args) != 3:
        logging.error(' Invalid number of arguments\nExamples:\n\t- 2str \t<NUMBER>\n\t- 2int \t<TEXT>\n')
        sys.exit(1)
    command = args[1]
    value = args[2]
    if command not in ['2int', '2str']:
        logging.error(f' Invalid command "{command}". Valid commands are 2int and 2str')
        sys.exit(1)
    if command == '2str':
        try:
            print(str_representation(value))
        except ValueError as e:
            logging.error(f'An error eccured: {e}')
    else:
        try:
            print(int_representation(value))
        except ValueError as e:
            logging.error(f'An error eccured: {e}')


    
