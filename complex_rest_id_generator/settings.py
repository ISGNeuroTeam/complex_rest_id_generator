import configparser

from pathlib import Path
from core.settings.ini_config import merge_ini_config_with_defaults

default_ini_config = {
    'logging': {
        'level': 'INFO'
    },
    'db_conf': {
        'host': 'localhost',
        'port': '5432',
        'database':  'id_generator_sequence',
        'user': 'id_generator',
        'password': 'password'
    }
}

config_parser = configparser.ConfigParser()

config_parser.read(Path(__file__).parent / 'id_generator.conf')

# convert to dictionary
config = {s: dict(config_parser.items(s)) for s in config_parser.sections()}

ini_config = merge_ini_config_with_defaults(config, default_ini_config)

DB_INFO = {
    'host': ini_config['db_conf']['host'],
    'port': ini_config['db_conf']['port'],
    'database': ini_config['db_conf']['database'],
    'user': ini_config['db_conf']['user'],
    'password': ini_config['db_conf']['password'],
}

# configure your own database if you need
# DATABASE = {
#         "ENGINE": 'django.db.backends.postgresql',
#         "NAME": ini_config['db_conf']['database'],
#         "USER": ini_config['db_conf']['user'],
#         "PASSWORD": ini_config['db_conf']['password'],
#         "HOST": ini_config['db_conf']['host'],
#         "PORT": ini_config['db_conf']['port']
# }