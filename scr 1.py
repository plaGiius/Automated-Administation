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
search1.send_keys("20Z317")
search1.send_keys(Keys.RETURN)

search2 = browser.find_element_by_name("txtpwdcheck")
search2.send_keys("18APR02")
search2.send_keys(Keys.RETURN)

link = browser.find_element_by_name("abcd3")
link.click()

academic = browser.find_element_by_id("Title1_Menu1-menuItem002")
academic.click()

camarks = browser.find_element_by_id("Title1_Menu1-menuItem002-subMenu-menuItem002")
camarks.click()

browser.switch_to.alert.accept()

mytable = browser.find_element_by_id("Tblsemfees")
print(mytable.text)

browser.quit()
