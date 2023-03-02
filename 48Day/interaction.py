from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Main_Page")
total_num_of_articles = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
print(total_num_of_articles.text)
# total_num_of_articles.click()

# all_portals = driver.find_element(By.LINK_TEXT, "All portals")
# all_portals.click()

search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)