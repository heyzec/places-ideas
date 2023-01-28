import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from uploader.drop_files import drop_files

def upload(driver, kml_string):
    driver.get("https://www.google.com/maps/d/edit?hl=en&mid=11K05tU0YGJaRkl1wMBiGusmBnUYlXpQ&ll=1.3750772054467364%2C103.71801429300284&z=18")

    btn_new_layer = (By.ID, "map-action-add-layer")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(btn_new_layer))
    time.sleep(1)
    driver.find_element(*btn_new_layer).click()
    print("clicked")

    time.sleep(5)
    btn_import = (By.XPATH, "//div[text()='Import']")
    # There may be hidden import buttons, so we select last, since it is definitely an empty layer, so button will be visible.
    btns = driver.find_elements(*btn_import)
    for btn in reversed(btns):
        if btn.get_attribute("id").endswith('layerview-import-link'):
            btn.click()
            break
        

    frames = driver.find_elements(By.TAG_NAME, 'iframe')
    driver.switch_to.frame(frames[-1])
    drop_zone = (By.ID, ":o.upload-container")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(drop_zone))
    drop_zone = driver.find_element(*drop_zone)


    drop_zone.drop_files("/home/heyzec/Desktop/places-ideas/out.kml")

    btn = driver.find_element(*btn_import)
    btn.send_keys("Test")
