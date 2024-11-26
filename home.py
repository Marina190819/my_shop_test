# Home: добавление комментария

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get ('https://practice.automationtesting.in')
driver.implicitly_wait(5)
driver.execute_script("window.scrollBy(0, 800);")
sel_ruby = driver.find_element_by_css_selector('.products>.post-160>a>h3')
sel_ruby.click()
driver.execute_script("window.scrollBy(0, 500);")
reviews = driver.find_element_by_class_name('reviews_tab')
reviews.click()
star = driver.find_element_by_class_name('star-5')
star.click()
comment = driver.find_element_by_id('comment')
comment.send_keys('Nice book!')
name = driver.find_element_by_id('author')
name.send_keys('Marina')
email = driver.find_element_by_id('email')
email.send_keys('test.email@mail.ru')
submit = driver.find_element_by_id('submit')
submit.click()
driver.quit()
