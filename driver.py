from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

def get_driver():
    profile_path = "/media/D/Common AppData/Firefox/profile"
    options = Options()
    options.add_argument(f"--profile {profile_path}")
    driver = Firefox(options=options)
    return driver
