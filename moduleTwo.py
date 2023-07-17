from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://techwithtim.net")

search = driver.find_element(By.NAME, "s")
search.send_keys("test")
search.send_keys(Keys.RETURN)

try :
    main = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )

    articles = main.find_element(By.TAG_NAME, "articles")
    for article in articles :
        header = article.find_element(By.CLASS_NAME,"entry-summary")
        print(header.text)

finally:
    driver.quit()    