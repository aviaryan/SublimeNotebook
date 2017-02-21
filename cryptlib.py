import base64
from getpass import getpass
import os

EXTRA_STR = 'ENCo0D#DT{xTCh$cKe>'


def encode(key, clear):
    st = ''
    clear += EXTRA_STR
    incr = get_key_hash(key)
    for _ in clear:
        st += chr(incr + ord(_))
    return base64.b64encode(st.encode('utf-8')).decode('utf-8') 


def decode(key, enc):
    st = ''
    enc = base64.b64decode(enc).decode('utf-8')  # dont know why urlsafe decode doesn't work
    incr = get_key_hash(key)
    for _ in enc:
        st += chr(ord(_) - incr)
    if not st.endswith(EXTRA_STR):
        return None
    else:
        return st[:-1 * len(EXTRA_STR)]


def get_key_hash(key):
    c = 0
    for _ in key:
        c += ord(_)
    return c % 20


def get_file_list():
    listFiles = []
    for dirpath, dnames, fnames in os.walk('./'):
        for f in fnames:
            if not (f.endswith('.txt') or f.endswith('.md')):
                continue
            listFiles.append(os.path.join(dirpath, f))
    return listFiles


def update_file(funcptr, flist, key):
    failed = False
    for file in flist:
        fptr = open(file, 'r')
        data = fptr.read()
        fptr.close()
        fptr = open(file, 'w')
        newData = funcptr(key, data)
        if newData is None:
            newData = data
            failed = True
            print('FAIL')
        fptr.write(newData)
        fptr.close()
        # check if failed
        if failed:
            break
    return failed


def get_key():
    key = ''
    while key == '':
        key = getpass('Enter key > ')
    return key
