# 웹 크롤링
# pip install requests
# pip install beautifulsoup4
# pip install lxml

# import : 모듈, 패키지를 포함하는 키워드
import requests
from bs4 import BeautifulSoup
           
           
url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105"
html = requests.get(url)

print(html)


# html 분석
# soup = BeautifulSoup(html.text, 'lxml')

# # 선택자로 지정해서 태그 가져오기
# newsList = soup.select('.sh_item')

# for news in newsList:
#     print(news)
   