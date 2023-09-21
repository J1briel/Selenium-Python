from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="../drivers/chromedriver")
driver.implicity_wait(5)

driver.get("https://jqueryui.com/droppable/")
driver.switch_to.frame(0)

src = driver.find_element_by_css_selector("#draggable")
trgt = driver.find_element_by_css_selector("#droppable")

a = ActionChains(driver)
a.drag_drop(src, trgt)
a.perform()





///identify the text in the specific frame box  

from selenium import webdriver
driver = webdriver.Chrome(executable_path="../drivers/chromedriver")

driver.implicitly_wait(5)

#website url 
driver.get("https://the-internet.herokuapp.com/nested_frames")
driver.switch_to.frame('frame-bottom')

#identify source element
s = driver.find_element_by_tag_name("body")
t = s.text

print("Text is: " + t)

driver.quit()

                                    
