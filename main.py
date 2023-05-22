import requests
from bs4 import BeautifulSoup


group = "radioenergy"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

url = f'https://vk.com/{group}'

response = requests.get(url, headers=headers)

print(response.status_code)


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Инициализация драйвера
driver = webdriver.Chrome()

# Перейти на страницу группы VK
driver.get(url)

# Ждать, пока страница загрузится
time.sleep(2)

# Прокрутить страницу вниз для загрузки всех постов
last_height = driver.execute_script("return document.body.scrollHeight")

datesSet = set()

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    new_height = driver.execute_script("return document.body.scrollHeight")
    res = [a.text for a in driver.find_elements(By.XPATH, '//time') if a.text]
    if new_height == last_height or res[-1] <= '1 янв 2023':
        break
    datesSet = datesSet.union(res)
    last_height = new_height
    print(datesSet)

# Найти все элементы, соответствующие дате постов в группе
dates = driver.find_elements(By.XPATH, '//time')

# Вывести даты всех найденных постов
for date in dates:
    print(date.text)

# Закрыть браузер
driver.quit()
