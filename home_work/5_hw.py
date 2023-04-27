from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


url = 'https://www.saucedemo.com/'

service = Service(executable_path='C:/chromedriver/chromedriver')  # указываем путь до драйвера
browser = webdriver.Chrome(service=service)
browser.get(url)

#Login

Username = browser.find_elements(By.ID, 'user-name')
if Username is None:
    print('"Элемент не найден')
else:
    print('Элемент найден')

#Password

Pass = browser.find_elements(By.ID, 'password')
if Pass is None:
    print('"Элемент не найден')
else:
    print('Элемент найден')

#Submit
Button = browser.find_elements(By.ID, 'login-but')
if Button is None:
    print('"Элемент не найден')
else:
    print('Элемент найден')

#sd_search = browser.find_element(By.ID, 'user-name')
#sd_search.send_keys('Vadim')
#sd_search.send_keys(Keys.ENTER)