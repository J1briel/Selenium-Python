import time as t
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://seleniumplayground.practiceprobs.com/")
t.sleep(10)
driver.close()
