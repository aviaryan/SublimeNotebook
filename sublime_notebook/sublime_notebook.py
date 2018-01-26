#!/Users/aviaryan/miniconda3/bin/python

"""
Sublime Notebook Manager
v1.0.0
"""

import os
from sys import exit
from .cryptlib import get_file_list, encode, update_file, get_key, decode
from .message import print_info


FLAG = 'sublime_notebook/FLAG_FILE'


def createFlagFile():
	fptr = open(FLAG, 'w')
	fptr.write('')
	fptr.close()


def main():
	"""
	Executes Sublime Notebook
	"""
	if not os.path.exists(FLAG):
		# new case
		# or decrypted state in power fail
		print('Not encrypted, encrypting ....')
		key = get_key()
		print('Re-enter key')
		key2 = get_key()
		if key != key2:
			print_info('Keys don\'t match, exiting')
			exit(1)
		update_file(encode, get_file_list(), key2)
		createFlagFile()
	else:
		# encrypted already
		print('Encrypted. Enter key to unlock')
		key = get_key()
		failStatus = update_file(decode, get_file_list(), key)
		if failStatus:
			print('You entered wrong key. Fuck off!')
			exit(2)
		os.remove(FLAG)
		# decoded, wait to close
		print_info('Notes have been decrypted')
		ans = ''
		while (True):
			ans = input('Press "e" to encrypt again\nPress"d" to stay decrypted (this disables Sublime Notebook encryption)\n> ')
			if ans == 'd' or ans == 'e':
				break
		if ans == 'e':
			# encrypt
			update_file(encode, get_file_list(), key)
			createFlagFile()
		else:
			# disable sublime notebook
			# exit as-is
			pass
