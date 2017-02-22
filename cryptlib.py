import base64
from getpass import getpass
import os

EXTRA_STR = 'ENCo0D#DT{xTCh$cKe>'
ENCODED_IDF = '=*=EnC0d3dH3aDer==*'


def encode(key, clear):
    st = ''
    if clear.startswith(ENCODED_IDF):  # already encoded, no need to encode
        return clear
    clear += EXTRA_STR  # used to check if decrypt is correct
    incr = get_key_hash(key)
    for _ in clear:
        st += chr(incr + ord(_))
    return ENCODED_IDF + base64.b64encode(st.encode('utf-8')).decode('utf-8') 


def decode(key, enc):
    st = ''
    if not enc.startswith(ENCODED_IDF):  # not encoded, so not decode
        return enc
    enc = enc[len(ENCODED_IDF):]  # trim out idf
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
        if dirpath.endswith('/public') or (dirpath.find('/public/') > -1):  # skip public notes
            continue
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
            print('Failed decrypting %s' % file)
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
