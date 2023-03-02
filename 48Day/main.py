from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome()
driver.get("https://www.python.org/")
# h = driver.find_elements("id", "id_name")
search_bar = driver.find_element("name", "q")
print(search_bar.tag_name)
print(search_bar.get_attribute("placeholder"))

# finding element by class
title = driver.find_element(By.CLASS_NAME, "widget-title")
print(title.text)

# finding element by css selector
doc_link = driver.find_element(By.CSS_SELECTOR, "a.readmore")
print(doc_link.text)

# finding element by xpath
xpath_link = driver.find_element(By.XPATH, '//*[@id="touchnav-wrapper"]/header/div/div[3]/p/a')
print(xpath_link.text)

# close only one tab
# driver.close()
# close all tabs
# driver.quit()
