from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://google.co.in")
search = driver.find_element(By.CLASS_NAME, "gLFyf")
time.sleep(2)
search.send_keys("Abhishek")
time.sleep(1)
search.send_keys(Keys.RETURN)

time.sleep(5)

driver.quit()