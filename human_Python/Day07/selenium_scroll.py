import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

url = 'https://pokemonkorea.co.kr/pokedex'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(2)

count = 16

# 처음 데이터
info_list = driver.find_elements(By.CSS_SELECTOR, '#pokedexlist .bx-txt h3')

html_text = ''
for item in info_list:
    tag = item.get_attribute('outerHTML')
    html_text += tag
    
soup = BeautifulSoup(html_text, 'html.parser')
print( type( soup ))

no_list_tag = soup.select('p')
no_list = []
for item in no_list_tag:
    no_list.append(item.text)


name_list = []

for item in soup:
    name_list.append( item.contents[1] )
    
    
###
prev = 0
now = 0
# for i in range(1, 11):
while True:
    # 스크롤 맨 아래로 이동
    script = '''
                document.body.scrollIntoView(false);
             '''
    driver.execute_script(script)
    
    
    time.sleep(2)
    info_list = driver.find_elements(By.CSS_SELECTOR, '#pokedexlist .bx-txt h3')
    
    
    # 이전 리스트 요소 개수와 현재 리스트 요소개수가 같으면 
    # 더 이상 데이터가 없으므로 종료
    now = len(info_list)
    if now == prev:
        break
    prev = now
    
    info_list = info_list[-count:]
    
    
    html_text = ''
    for item in info_list:
        tag = item.get_attribute('outerHTML')
        html_text += tag
        
    soup = BeautifulSoup(html_text, 'html.parser')
    
    no_list_tag = soup.select('p')
    for item in no_list_tag:
        no_list.append(item.text)
    
    for item in soup:
        name_list.append( item.contents[1] )
    

print(no_list)
print(name_list)

time.sleep(10)

