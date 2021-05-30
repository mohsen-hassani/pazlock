'''Simple NOT SECURE password locker 

    This script change the representation of your password to
    its integer (10-base), then combine with the 10-based key 
    in chuncks with length of key. One left zero padding will
    apply to insure all chunks have same length

'''
import sys
import logging
from inttser import str_representation, int_representation

def lock_password(password, key):
    '''Lock password with key '''
    key = int_representation(key)
    pad = len(key)
    key = int(key)
    passint = int_representation(password)
    new_passint = ''
    for i in range(0, len(passint), pad):
        chunck = passint[i: i + pad]
        chunck_num = int(chunck)
        new_chunck = str(chunck_num + key)
        new_chunck = new_chunck.zfill(pad+1)
        new_passint += new_chunck
    return new_passint


def unlock_password(number, key):
    '''Unlock password with key '''
    key = int_representation(key)
    pad = len(key)
    key = int(key)
    new_number = ''
    for i in range(0, len(number), pad+1):
        chunck = number[i: i + pad + 1]
        chunck_num = int(chunck)
        new_chunck = str(chunck_num - key).zfill(pad)
        new_number += new_chunck
    return str_representation(new_number)

if __name__ == '__main__':
    args = sys.argv
    if len(args) != 4:
        msg = 'Error: Invalid number of arguments\nExample:\n\t- <OPTION> <PASSWORD> <LOCK_KEY>\n\n'
        msg += 'Options:\n\tlock\tlock your password with key\n\tunlock\tunlock your password with key'
        logging.error(msg)
        sys.exit(1)
    command = args[1]
    password = args[2]
    key = args[3]
    if command not in ['lock', 'unlock']:
        logging.error(f'Error: Invalid command "{command}". Valid commands are "lock" and "unlock"')
        sys.exit(1)
    if command == 'lock':
        print(lock_password(password, key))
    else:
        print(unlock_password(password, key))
        
