#Registration_login: регистрация аккаунта
#
#
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get ('https://practice.automationtesting.in')
# driver.implicitly_wait(5)
# my_account = driver.find_element_by_link_text('My Account')
# my_account.click()
# name = driver.find_element_by_id('reg_email')
# name.send_keys('nemesh.marisha@gmail.com')
# password = driver.find_element_by_id('reg_password')
# password.send_keys('tqNv7d4A!')
# register = driver.find_element_by_name('register')
# register.click()
# driver.quit()
#
# Registration_login: логин в систему

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get ('https://practice.automationtesting.in')
driver.implicitly_wait(5)
my_account = driver.find_element_by_link_text('My Account')
my_account.click()
log_name = driver.find_element_by_id('username')
log_name.send_keys('nemesh.marisha@gmail.com')
log_password = driver.find_element_by_id('password')
log_password.send_keys('tqNv7d4A!')
login = driver.find_element_by_name('login')
login.click()
logout = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, "Logout")))
driver.quit()
