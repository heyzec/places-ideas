import time

from numpy import nan
import pandas as pd
import pyperclip as pc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from functions import plus_code_to_coord

def geocode(driver):
    base_path = "data/places.xlsx"
    df = pd.read_excel(base_path, 'Sheet1')

    driver.get("https://www.google.com/maps")

    for index, row in df.iterrows():
        if row["coordinates"] is not nan:
            print("skipping becuz")
            print(repr(row['coordinates']))
            continue
        print("Getting data for ", row['name'], row['area'])

        keywords = f"{row['name']} {row['area']}"
        searchbar = driver.find_element(By.ID, "searchboxinput")
        searchbar.send_keys(keywords)
        driver.find_element(By.ID, "searchbox-searchbutton").click()
        

        btn_share = (By.XPATH, "//img[contains(@alt, 'Share')]")
        WebDriverWait(driver, 100).until(EC.presence_of_element_located(btn_share))
        time.sleep(1)  # Sometimes, the map is still zooming in.
        driver.find_element(*btn_share).click()
        
        btn_copy_link = (By.XPATH, "//button[contains(text(), 'Copy link')]")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(btn_copy_link))
        driver.find_element(*btn_copy_link).click()
        gmaps_link = pc.paste()

        driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Close')]").click()
        
        btn_plus_code = (By.XPATH, "//button[contains(@aria-label, 'Copy plus code')]")

        WebDriverWait(driver, 10).until(EC.presence_of_element_located(btn_plus_code))
        driver.find_element(*btn_plus_code).click()
        plus_code = pc.paste()
        
        coordinates = plus_code_to_coord(plus_code)
        df.at[index, "coordinates"] = f"{coordinates[0]}, {coordinates[1]}"
        df.at[index, "gmaps"] = gmaps_link

        driver.find_element(By.XPATH, "//a[contains(@aria-label, 'Clear search')]").click()
        

    # This preserves the formatting of the sheet
    # https://stackoverflow.com/a/73899857
    with pd.ExcelWriter('data/places.xlsx', engine='openpyxl',
                        mode='a', if_sheet_exists='overlay') as writer:
        df.to_excel(writer, sheet_name='Sheet1', startrow=1,
                    startcol=0, header=False, index=False)
