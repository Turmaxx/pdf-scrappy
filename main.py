# imports
# driver and service imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
# support imports
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# exception imports
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
# other imports
import time
from os import system, name

def clear():
    # clear terminal for windows os
    if name == 'nt':
        _ = system('cls')

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)
driver.get("https://ca1lib.org/")

clear()

search = driver.find_element(By.ID,"searchFieldx")
search.clear()
search.send_keys('Rust')
search.send_keys(Keys.RETURN)

book = input("Enter A name of a book to download: ")

try:
    ignored = (NoSuchElementException, StaleElementReferenceException)
    search_result = WebDriverWait(driver, 10,ignored_exceptions=ignored).until(
        EC.presence_of_element_located((By.LINK_TEXT, book)))
    search_result.click()

    for i in range(3):
        try:
            driver.find_element(By.LINK_TEXT,"Download (pdf, 8.65 MB)").click()
            time.sleep(2)
            driver.find_element(By.ID, "download").click()
            break
        except StaleElementReferenceException:
            print("Not Found")

except:
    time.sleep(10)
    driver.quit()
