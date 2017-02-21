#!/Users/aviaryan/miniconda3/bin/python
import os
from sys import exit
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
		key = get_key()
		print('Re-enter key')
		key2 = get_key()
		if key != key2:
			print('Keys don\'t match, exiting')
			exit(1)
		update_file(encode, get_file_list(), key2)
		createFlagFile()
	else:
		# encrypted already
		print('Encrypted, give key to unlock')
		key = get_key()
		failStatus = update_file(decode, get_file_list(), key)
		if failStatus:
			print('You entered wrong key. FO')
			exit(2)
		os.remove(FLAG)
		# decoded, wait to close
		ans = ''
		while ans != 'e':
			ans = input('Press e to encrypt again > ')
		# encrypt
		update_file(encode, get_file_list(), key)
		createFlagFile()
