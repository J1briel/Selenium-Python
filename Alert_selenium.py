from selenium import webdriver
from selenium.webdriver.common.alert import Alert
driver = webdriver.Chrome()
driver.implicitly_wait(0.8)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
l = driver.find_element_by_xpath("//*[text()='Click for JS Prompt']")
l.click()

a = Alert(driver)
print(a.text)

a.send_keys("Bacon")
a.dismiss()
l.click()
a.accept()
driver.quit()
