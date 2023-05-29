import configparser
from django.conf import settings
import os

def read_ini_file():
    file_path = os.path.join(settings.BASE_DIR, 'config/file.ini')
    config = configparser.ConfigParser()
    config.read(file_path)
    return config

