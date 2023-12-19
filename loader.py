from minilogger import Console
from getpass    import getuser
from os.path    import exists
from json       import load, dump
from os         import makedirs


FORCE_RELOAD = True

platform = 'nt' if exists('C:/') else 'unix'

Console.log(f'Detected platform: {platform}', 'Loader', 'D')

data_folder = f'C:/Users/{getuser()}/AppData/Local/R1senDev/CalcuVault' if platform == 'nt' else f'/usr/local/calcuvault/{getuser()}'

try:
	makedirs(f'{data_folder}/data/files/')
	Console.log(f'Created path: {data_folder}/data/files/', 'Loader', 'I')
except FileExistsError:
	Console.log(f'Path {data_folder}/data/files/ already exists', 'Loader', 'D')

if FORCE_RELOAD or not exists(f'{data_folder}/config.json'):
	
	if FORCE_RELOAD:
		Console.log(f'FORCE_RELOAD is hardcoded to True. config.json will be recreated on each start of application', 'Loader', 'W')
	else:
		Console.log(f'config.json is not exists: defaults will be used', 'Loader', 'I')
	
	config = {
		'passkey': '666228',
		'appearance': {
			'fg_color': [255, 255, 255],
			'bg_color': [20, 20, 20]
		}
	}
	
	with open(f'{data_folder}/config.json', 'w') as file:
		dump(config, file)

	Console.log(f'Created config.json', 'Loader', 'I')

else:

	with open(f'{data_folder}/config.json', 'r') as file:
		config = load(file)
	Console.log(f'Loaded config.json', 'Loader', 'I')

if not exists(f'{data_folder}/data/storage.json'):
	
	storage_description = {}
	with open(f'{data_folder}/data/storage.json', 'w') as file:
		dump(storage_description, file)
	
	Console.log(f'Created storage descriptor JSON file', 'Loader', 'I')

else:
	
	with open(f'{data_folder}/data/storage.json', 'r') as file:
		storage_description = load(file)
	
	Console.log(f'Loaded storage description from JSON file', 'Loader', 'I')

Console.log(f'Loading done', 'Loader', 'I')