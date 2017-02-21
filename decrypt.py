#!/Users/aviaryan/minconda3/bin/python
from cryptlib import get_file_list, decode, update_file, get_key

flist = get_file_list()
print(flist)
update_file(decode, flist, get_key())
