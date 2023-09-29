from os import environ

API_ID = int(environ.get('API_ID', '9830058'))
API_HASH = environ.get('API_HASH', '908e8bff7c8f6ecd5d0ab989f78134fc')
BOT_TOKEN = environ.get('BOT_TOKEN', '6471679179:AAGZRVM4gL_F4p5mili_zgR11a7LNXgJDpw')
FILE_CAPTION = environ.get('FILE_CAPTION', '<code>{file_name}</code>')
OWNER = int(environ.get('OWNER', '6616684260'))
PRIVATE_BOT = bool(environ.get('PRIVATE_BOT', False))

