import configparser
import os
import shutil
import time

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

NEW_PROFILE_PATH = '/tmp/profile'

def create_profile():
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

    os.mkdir(NEW_PROFILE_PATH)

    os.system(f'timeout 3 firefox --profile {NEW_PROFILE_PATH}')
    time.sleep(3)
    shutil.copy2(f"{original_profile_path}/cookies.sqlite", f"{NEW_PROFILE_PATH}")

def get_driver():
    options = Options()
    options.add_argument(f"--profile")
    options.add_argument(f"{NEW_PROFILE_PATH}")
    driver = Firefox(options=options)
    return driver
