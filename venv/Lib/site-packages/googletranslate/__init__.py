"""Free Google Translate API for Python. Translates totally free of charge."""
__all__ = 'Translator',
__version_info__ = 2, 1, 2
__version__ = '.'.join(str(v) for v in __version_info__)


import os
from googletranslate.client import Translator
from googletranslate.constants import LANGUAGES

config_path = os.path.expanduser('~/.googletrans')
if not os.path.isfile(config_path):
    with open(config_path, 'w') as f:
        f.write('translate.google.com')

with open(config_path, 'r') as f:
    translator = Translator(map(lambda x: x.strip(), list(f)))
