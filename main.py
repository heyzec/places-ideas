from geocoder.geo import geocode

from driver import create_profile, get_driver
from kml.kml_generator import generate_kml
from uploader.uploader import upload

create_profile()
driver = get_driver()
geocode(driver)
output = generate_kml()
upload(driver, "")