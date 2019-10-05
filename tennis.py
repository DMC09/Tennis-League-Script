from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time


#  set up
#  Script


user = ""
pwd = ""
browser = webdriver.Chrome("/Users/dharminchauhan/Downloads/chromedriver")
browser.get('http://mon.pythonanywhere.com/accounts/login/?next=/league/')
elem = browser.find_element_by_id("id_username")
elem.send_keys(user)
elem = browser.find_element_by_id("id_password")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
browser.implicitly_wait(10)
time.sleep(0.5)
elem = browser.find_element_by_xpath("/html/body/div[3]/h4/form/input[3]")
elem.click()
browser.implicitly_wait(5)
browser.quit()
