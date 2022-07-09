import selenium
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromedriver = '/usr/local/bin/chromedriver'
browser = webdriver.Chrome(chromedriver)
browser.get("https://ecampus.psgtech.ac.in/studzone2/AttWfLoginPage.aspx")
print(browser.title)
search1 = browser.find_element_by_name("txtusercheck")
search1.send_keys("20Z302")
search1.send_keys(Keys.RETURN)

search2 = browser.find_element_by_name("txtpwdcheck")
search2.send_keys("29MAY02")
search2.send_keys(Keys.RETURN)
