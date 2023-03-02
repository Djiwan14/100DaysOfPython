from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.python.org/")
date_name = {
    "number" : {
    "time": "",
    "name": ""
}
}
event_times = driver.find_elements(By.CSS_SELECTOR, 'time.event-widget')
event_names = driver.find_elements(By.CSS_SELECTOR, "li a.event-widget")
events = {}
for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }
print(events)