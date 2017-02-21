#!/Users/aviaryan/miniconda3/bin/python
import os
from cryptlib import get_file_list, encode, update_file, get_key, decode

FLAG = 'FLAG_FILE'


def createFlagFile():
	fptr = open(FLAG, 'w')
	fptr.write('')
	fptr.close()


if __name__ == '__main__':

	if not os.path.exists(FLAG):
		# new case
		# or decrypted state in power fail
		print('Not encrypted, encrypting....')
		update_file(encode, get_file_list(), get_key())
		createFlagFile()
	else:
		# encrypted already
		print('Encrypted, give key to unlock')
		key = get_key()
		update_file(decode, get_file_list(), key)
		os.remove(FLAG)
		# decoded, wait to close
		ans = ''
		while ans != 'e':
			ans = input('Press e to encrypt again > ')
		# encrypt
		update_file(encode, get_file_list(), key)
		createFlagFile()
