import configparser
import os
import shutil
import time

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

CLONED_PROFILE_PATH = '/tmp/profile'

def get_driver():
    filename = '/home/heyzec/.mozilla/firefox/profiles.ini'
    config = configparser.ConfigParser()
    with open(filename, 'r') as f:
        config.read_file(f)
            
    original_profile_path = config.sections()[0]
    first_section = config.sections()[0]
    key_locked = config[first_section]['Locked']
    if key_locked != '1':
        print("Unable to detect default profile.")
        exit()
    original_profile_path = config[first_section]['Default']

    profile_path = CLONED_PROFILE_PATH
    os.mkdir(profile_path)

    os.system(f'timeout 3 firefox --profile {profile_path}')
    time.sleep(3)
    shutil.copy2(f"{original_profile_path}/cookies.sqlite", f"{profile_path}")

    options = Options()
    options.add_argument(f"--profile")
    options.add_argument(f"{profile_path}")
    driver = Firefox(options=options)
    return driver
