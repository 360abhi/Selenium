from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.minimize_window()
# driver.get("https://www.google.co.in")
# print("driver title: ", driver.title)

driver = webdriver.Chrome()
driver.get("https://www.google.co.in")
print(driver.title)
print(driver.current_url)

driver.quit()