import json
from sublime_notebook import SETTINGS_PATH, VERSION
from .message import print_err


class Settings:
	"""
	Settings module
	"""
	default_json = {
		'public_folders': ['*'],
		'private_folders': ['diary'],
		'is_encrypted': False,
		'version': VERSION
	}
	json = default_json.copy()
	where_star = 'public'
	file = SETTINGS_PATH

	def __init__(self, file=None):
		if file:
			self.file = file
		self.load_file()

	def load_file(self):
		"""
		Loads file as JSON
		"""
		try:
			fp = open(self.file, 'r')
			data = fp.read()
			self.json = json.loads(data)
			fp.close()
			self.find_star()
		except Exception as e:
			# load default settings
			print_err('JSON Exception occurred: ' + str(e))

	def find_star(self):
		if Settings._find_in_array('*', self.json['private_folders']):
			self.where_star = 'private'
		else:  
			# default behavior public
			self.where_star = 'public'

	def check_folder_private(self, dirname):
		st = Settings._find_in_array(dirname, self.json['private_folders'])
		if st:
			return True
		st = Settings._find_in_array(dirname, self.json['public_folders'])
		if st:
			return False
		# star situation
		return True if self.where_star == 'private' else False

	def change_encrypted_status(self, status):
		self.load_file()
		self.json['is_encrypted'] = status
		self.save_settings()

	def get_encrypted_status(self):
		return self.json['is_encrypted']

	def save_settings(self):
		Settings._write_settings(self.json, self.file)

	def upgrade_settings(self):
		if VERSION > self.json['version']:
			new = self.default_json.copy()
			new.update(self.json)  # only adds new keys
			self.json = new.copy()
			self.json['version'] = VERSION  # upgrade version again
			self.save_settings()
			return True
		return False

	@staticmethod
	def _find_in_array(item, arr):
		status = False
		for i in arr:
			if item == i:
				status = True
				break
		return status

	@staticmethod
	def _create_default_file():
		Settings._write_settings(Settings.json, Settings.file)

	@staticmethod
	def _write_settings(setting, file):
		data = json.dumps(setting, indent=4, sort_keys=True)
		fp = open(file, 'w')
		fp.write(data)
		fp.close()
