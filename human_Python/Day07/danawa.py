from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

keyword = input()
url = f'https://search.danawa.com/dsearch.php?k1={keyword}'


# url 이동
driver.get(url)