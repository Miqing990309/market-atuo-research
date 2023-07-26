"""Common module to read/write per-user configuration files.
"""

import configparser
import logging
import os
import os.path
import sys
from typing import List

# current dir
current_path = os.getcwd()
# Path
config_path = os.path.join(current_path, "config")
CONFIG_DIR = config_path
CONFIG_FILE = os.path.join(CONFIG_DIR, f'{os.path.basename(sys.argv[0])}.conf')

class ConfigFile(object):
    def __init__(self, path: str=CONFIG_FILE):
        self.path = path
        self.conf = configparser.ConfigParser()
        if not (os.path.exists(CONFIG_DIR) and os.path.isdir(CONFIG_DIR)):
            os.mkdir(CONFIG_DIR)

        # read from an existing file (if exist), or create a new one; note
        # that the file handle is NOT kept open, so write() has to be called
        # after any changes
        self.read()

        # if there is no "settings" section, create one
        if 'settings' not in self.conf:
            self.conf['settings'] = {}

    def read(self):
        self.conf.read(self.path, encoding='utf-8')

    def write(self):
        if not (os.path.exists(CONFIG_DIR) and os.path.isdir(CONFIG_DIR)):
            os.mkdir(CONFIG_DIR)

        with open(self.path, 'w') as f:
            self.conf.write(f)

    def set(self, key: str, value, section='settings'):
        """Set a value, given key and section. If value is a list of string,
        automatically convert this into a multiline string."""

        # TODO: handle conversion to string from non-string data automatically
        if type(value) == list:
            v = '\n'.join([str(x) for x in value])
        else:
            v = str(value)
        self.conf[section][key] = v

    def get(self, key: str, fallback: str=None, section: str='settings') -> str:
        """Read a value, given key and section. If specified, the fallback
        value will be returned if the key+value does not exist in the
        section."""

        if fallback:
            return self.conf[section].get(key, fallback)
        return self.conf[section].get(key)

    def get_multiline(self, key: str, section: str='settings') -> List[str]:
        """Read a multiline value, given key and section. This will
        automatically convert the value to a list of strings."""

        value = self.conf[section].get(key, fallback='').split('\n')
        # configparser will sometimes write the first value in the line after
        # the key, and this will be read back as an empty first line; skip
        # this empty entry
        if not value[0]:
            value = value[1:]
        return value
