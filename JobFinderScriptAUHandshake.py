#   Jarrett Tang
#   JobFinderScriptAUHandshake.py

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from . import credentials

#   loads browser with website
print("Starting browser...")
print("Loading Auburn Handshake...")
driver = webdriver.Firefox()
driver.get("https://auburn.joinhandshake.com/login")
assert "Handshake" in driver.title

#   next webpage
print("Loading Login Screen...")
elem = driver.find_element_by_link_text("Auburn University Student Login")
elem.click()
assert "Login - Authenticate" in driver.title

#   Logging In
#   element = username
print("Inputting user data...")
elem = driver.find_element_by_id("username")
elem.clear()
elem.send_keys(credentials.USERNAME)

#   element = password
elem = driver.find_element_by_id("password")
elem.clear()
elem.send_keys(credentials.PASSWORD)
elem.send_keys(Keys.RETURN)
print("Logging in...")
elem = WebDriverWait(driver, 30).until(
    EC.title_contains("Handshake")
)
assert "Handshake" in driver.title
print("Entered AU Handshake!!!")
#   7/20 17:47  finished navigating to homepage
#               need to navigate to job board lists
#               and recognize listings and then apply

#   jump into job listings


exit()
