# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.get("http://suninjuly.github.io/simple_form_find_task.html")
# button = driver.find_element(By.ID, "submit_button")

print("_________")
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import math
#
# link = "http://suninjuly.github.io/find_link_text"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     link = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
#     link.click()
#
#     input1 = browser.find_element(By.TAG_NAME, "input")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.NAME, "last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.CSS_SELECTOR, '.form-control.city')
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element(By.ID, "country")
#     input4.send_keys("Russia")
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()


print("_________")

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/huge_form.html")
#     elements = browser.find_elements(By.TAG_NAME, "input")
#     for element in elements:
#         element.send_keys("Мой ответ")
#
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#
# # не забываем оставить пустую строку в конце файла

# from selenium import webdriver
from selenium.webdriver.common.by import By
# import time
#
# link = "http://suninjuly.github.io/find_xpath_form"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     input1 = browser.find_element(By.TAG_NAME, "input")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.NAME, "last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.CSS_SELECTOR, '.form-control.city')
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element(By.ID, "country")
#     input4.send_keys("Russia")
#     button = browser.find_element(By.XPATH, "//div[6]/button[3]")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#
# # не забываем оставить пустую строку в конце файла

# import math
# import time
# from selenium import webdriver
#
#
# def calc(x):
#     return str(math.log(abs(12*math.sin(int(x)))))
#
#
# link = "http://suninjuly.github.io/math.html"
# browser = webdriver.Chrome()
# browser.get(link)
#
# x_element = browser.find_element(By.ID, 'input_value')
# x = x_element.text
# y = calc(x)
#
# element1 = browser.find_element(By.ID, 'answer')
# element1.send_keys(y)
#
# option1 = browser.find_element(By.CSS_SELECTOR,"[for='robotCheckbox']")
# option1.click()
# option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
# option2.click()
# option2 = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
# option2.click()
#
# time.sleep(5)
# browser.quit()


# from selenium import webdriver
# import math
#
# link = "http://suninjuly.github.io/get_attribute.html"
# browser = webdriver.Chrome()
# browser.get(link)
#
# # функция, которая находит значение выражения при заданном x
# def calc(x):
# 	return str( math.log( abs( 12 * math.sin( int(x) ) ) ) )
#
# # находим значение x для выполнения задания
# chest = browser.find_element(By.ID,"treasure")
# x_value = chest.get_attribute("valuex")
#
# # высчитываем результат для первого задания
# first_test_result = calc(x_value)
#
# # вводим ответ к первому тесту
# first_test_input = browser.find_element(By.ID,"answer")
# first_test_input.send_keys(first_test_result)
#
# # выбираем checkbox
# robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
# robot_checkbox.click()
#
# # выбираем radiobutton
# robot_radiobutton = browser.find_element(By.ID, "robotsRule")
# robot_radiobutton.click()
#
# # нажимаем кнопку отправить
# send_button = browser.find_element(By.CLASS_NAME, "btn-default")
# send_button.click()


# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
#
# link = "http://suninjuly.github.io/selects2.html"
# browser = webdriver.Chrome()
# browser.get(link)
#
# num1_element = browser.find_element(By.ID, 'num1')
# num1 = num1_element.text
# print(num1)
# num2_element = browser.find_element(By.ID, 'num2')
# num2 = num2_element.text
# print(num2)
# result = int(num1) + int(num2)
# print(result)
#
# select = Select(browser.find_element(By.ID, 'dropdown'))
# select.select_by_visible_text(str(result))
#
# option = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
# option.click()

#
# import math
# from selenium import webdriver
#
#
# def calc(x):
#     return str(math.log(abs(12*math.sin(int(x)))))
#
#
# link = "https://suninjuly.github.io/execute_script.html"
# browser = webdriver.Chrome()
# browser.get(link)
#
# x_element = browser.find_element(By.ID, 'input_value')
# x = x_element.text
# y = calc(int(x))
#
# button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
# browser.execute_script('window.scrollBy(0, 100);')
#
# element1 = browser.find_element(By.ID, 'answer')
# element1.send_keys(y)
#
# option1 = browser.find_element(By.ID, 'robotCheckbox')
# option1.click()
# option2 = browser.find_element(By.ID, "robotsRule")
# option2.click()
# button.click()

import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

element_1 = browser.find_element(By.CSS_SELECTOR,".form-control")
element_1.send_keys("Nick")

element_2 = browser.find_element(By.NAME,"lastname")
element_2.send_keys("Nick")

element_3 = browser.find_element(By.NAME,"email")
element_3.send_keys("Nick")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
element.send_keys(file_path)

button = browser.find_element(By.CSS_SELECTOR,".btn.btn-primary").click()
