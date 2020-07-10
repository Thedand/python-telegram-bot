from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

user = "LOGIN"  # change LOGIN
password = "PASSWORD"  # change PASSWORD

browser = webdriver.Chrome()  # browser Chrome
browser.get("https://online.agroprombank.com/Login.aspx")  # url page
browser.set_window_size(1920, 1080)  # resolution windows browser
u = browser.find_element_by_id("centralPanelPlaceHolder_userField")  # find element login user
u.send_keys(user, Keys.ARROW_DOWN)  # pass the value from "USER"
p = browser.find_element_by_id("centralPanelPlaceHolder_passwordField")  # find element password user
p.send_keys(password, Keys.ARROW_DOWN)  # pass the value from "PASSWORD"
enter = browser.find_element_by_id("centralPanelPlaceHolder_loginButton")  # find element login button
enter.click()  # click to login
sleep(5)  # timeout 5 sec

browser.close()  # close browser


