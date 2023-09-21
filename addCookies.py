from selenium import webdriver
  
# create webdriver object
driver = webdriver.Firefox()
  
driver.get("https://www.geeksforgeeks.org/")

driver.add_cookie({"name" : "foo", "value" : "bar"})
