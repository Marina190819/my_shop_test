# Shop: отображение страницы товара
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
# log_name = driver.find_element_by_id('username')
# log_name.send_keys('nemesh.marisha@gmail.com')
# log_password = driver.find_element_by_id('password')
# log_password.send_keys('tqNv7d4A!')
# login = driver.find_element_by_name('login')
# login.click()
# shop = driver.find_element_by_link_text('Shop')
# shop.click()
# kostil= driver.find_element_by_css_selector('.products.masonry-done>.product_cat-html>.woocommerce-LoopProduct-link>h3')
# kostil.click()
# some_element= WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "entry-title"), "HTML5 Forms"))
# if some_element is None:
#     print('Название не соответствует')
# else:
#     print('Название соответствует')
# driver.quit()


# Shop: количество товаров в категории
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
# log_name = driver.find_element_by_id('username')
# log_name.send_keys('nemesh.marisha@gmail.com')
# log_password = driver.find_element_by_id('password')
# log_password.send_keys('tqNv7d4A!')
# login = driver.find_element_by_name('login')
# login.click()
# shop = driver.find_element_by_link_text('Shop')
# shop.click()
# html=driver.find_element_by_link_text('HTML')
# html.click()
# hm= driver.find_elements_by_class_name('attachment-shop_catalog')
# print(len(hm))
# driver.quit()

# Shop: сортировка товаров

# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get ('https://practice.automationtesting.in')
# driver.implicitly_wait(5)
# my_account = driver.find_element_by_link_text('My Account')
# my_account.click()
# log_name = driver.find_element_by_id('username')
# log_name.send_keys('nemesh.marisha@gmail.com')
# log_password = driver.find_element_by_id('password')
# log_password.send_keys('tqNv7d4A!')
# login = driver.find_element_by_name('login')
# login.click()
# shop = driver.find_element_by_link_text('Shop')
# shop.click()
# selector= driver.find_element_by_name('orderby')
# value = selector.get_attribute('value')
# print ("value:", value)
# select = Select(selector)
# select.select_by_value("price-desc")
# selector= driver.find_element_by_name('orderby')
# value = selector.get_attribute('value')
# print ("value:", value)
# driver.quit()

#
#
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get ('https://practice.automationtesting.in')
# driver.implicitly_wait(5)
# my_account = driver.find_element_by_link_text('My Account')
# my_account.click()
# log_name = driver.find_element_by_id('username')
# log_name.send_keys('nemesh.marisha@gmail.com')
# log_password = driver.find_element_by_id('password')
# log_password.send_keys('tqNv7d4A!')
# login = driver.find_element_by_name('login')
# login.click()
# shop = driver.find_element_by_link_text('Shop')
# shop.click()
# android = driver.find_element_by_css_selector('[title="Android Quick Start Guide"]')
# android.click()
# old_price = driver.find_element_by_css_selector('del>.woocommerce-Price-amount.amount')
# old_price
# old_price_get_text = old_price.text
# assert "600" in old_price_get_text
# print("Цена соответствует 600")
# new_price = driver.find_element_by_css_selector('ins>.woocommerce-Price-amount.amount')
# new_price
# new_price_get_text = new_price.text
# assert "450" in new_price_get_text
# print("Цена соответствует 450")
# img = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "wp-post-image")) )
# img.click()
# krestik = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")) )
# krestik.click()
# driver.quit()

# Shop: проверка цены в корзине
#
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get ('https://practice.automationtesting.in')
# driver.implicitly_wait(5)
# shop = driver.find_element_by_link_text('Shop')
# shop.click()
# add_to = driver.find_element_by_css_selector('[data-product_id="182"].ajax_add_to_cart')
# add_to.click()
# time.sleep(3)
# bag_piece = driver.find_element_by_class_name('cartcontents')
# bag_piece_get_text = bag_piece.text
# assert '1' in bag_piece_get_text
# print ('Количество товаров соответствует 1')
# price = driver.find_element_by_css_selector('.wpmenucart-contents>.amount')
# price_get_text = price.text
# assert "180" in price_get_text
# print('Cтоимость 180')
# price.click()
# subtotal = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
#                     (By.CSS_SELECTOR, '[data-title="Subtotal"]>.woocommerce-Price-amount')))
# subtotal_get_text = subtotal.text
# print ('Стоимость корзины', subtotal_get_text)
# total = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
#                     (By.CSS_SELECTOR, 'strong>.woocommerce-Price-amount')))
# total_get_text = total.text
# print('Стоимость корзины с налогом', total_get_text)
# driver.quit()
#








# Shop: работа в корзине

# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get ('https://practice.automationtesting.in')
# driver.implicitly_wait(5)
# shop = driver.find_element_by_link_text('Shop')
# shop.click()
# driver.execute_script("window.scrollBy(0, 300);")
# add_to = driver.find_element_by_css_selector('[data-product_id="182"]')
# add_to.click()
# time.sleep(3)
# add_to_2 = driver.find_element_by_css_selector('[ data-product_id="180"]')
# add_to_2.click()
# bag = driver.find_element_by_id('wpmenucartli')
# bag.click()
# time.sleep(3)
# remove = driver.find_element_by_css_selector('[data-product_id="182"]')
# remove.click()
# undo = driver.find_element_by_link_text('Undo?')
# undo.click()
# line = driver.find_element_by_css_selector('tr:nth-child(1)>td>.quantity>.input-text')
# line.clear()
# line.send_keys('3')
# update = driver.find_element_by_name('update_cart')
# update.click()
# update = driver.find_element_by_name('update_cart')
# value = line.get_attribute('value')
# print ("value:", value)
# assert value == "3"
# time.sleep(3)
# apply_coupon = driver.find_element_by_name('apply_coupon')
# apply_coupon.click()
# error = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
#                     (By.CSS_SELECTOR, '.woocommerce-error>li')))
# print ('Сообщение найдено')
# driver.quit()

# Shop: покупка товара

# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get ('https://practice.automationtesting.in')
# driver.implicitly_wait(5)
# shop = driver.find_element_by_link_text('Shop')
# shop.click()
# driver.execute_script("window.scrollBy(0, 300);")
# add_to = driver.find_element_by_css_selector('[data-product_id="182"]')
# add_to.click()
# time.sleep(3)
# bag = driver.find_element_by_id('wpmenucartli')
# bag.click()
# proceed = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button")) )
# proceed.click()
# first_name = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "billing_first_name")) )
# first_name.send_keys('Marina')
# last_name = driver.find_element_by_id('billing_last_name')
# last_name.send_keys('Nemesh')
# phone = driver.find_element_by_id('billing_phone')
# phone.send_keys('89123456789')
# email = driver.find_element_by_id('billing_email')
# email.send_keys('nemesh@mail.ru')
# selector = driver.find_element_by_css_selector('.select2-arrow>[role="presentation"]')
# selector.click()
# write = driver.find_element_by_id('s2id_autogen1_search')
# write.send_keys('Malta')
# malta = driver.find_element_by_class_name('select2-match')
# malta.click()
# address = driver.find_element_by_id('billing_address_1')
# address.send_keys("Novaja")
# apartment = driver.find_element_by_id('billing_address_2')
# apartment.send_keys('11')
# town =driver.find_element_by_id('billing_city')
# town.send_keys('Volosovo')
# state = driver.find_element_by_id('billing_state')
# state.send_keys('Volosovski')
# postcode = driver.find_element_by_id('billing_postcode')
# postcode.send_keys('252525')
# driver.execute_script("window.scrollBy(0, 600);")
# time.sleep(3)
# check = driver.find_element_by_id('payment_method_cheque')
# check.click()
# place_order = driver.find_element_by_id('place_order')
# place_order.click()
# thank_you = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
#                     (By.CLASS_NAME, 'woocommerce-thankyou-order-received')))
# print('Сообщение о благодарности появилось')
# pay_method = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
#                     (By.CSS_SELECTOR, '.method>strong')))
# print('Информация о методе отображается')
# driver.quit()