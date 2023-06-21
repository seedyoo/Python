# 웹 크롤링
# pip install requests
# pip install beautifulsoup4
# pip install lxml

# import : 모듈, 패키지를 포함하는 키워드
import requests
from bs4 import BeautifulSoup
           
           
url = "http://www.cgv.co.kr/movies"
html = requests.get(url)

print(html)


# html 분석
soup = BeautifulSoup(html.text, 'lxml')

# 선택자로 지정해서 태그 가져오기
# movieList = soup.select('.sect-movie-chart .title')
movieList = soup.select('.box-contents')

for movie in movieList:
    # 영화제목
    title = movie.find(class_="title").get_text()
    # 예매율
    percent = movie.select('.score > .percent span')[0].get_text()
    # 개봉일자
    open_date = movie.select('.txt-info strong')[0].get_text()
    # open_date = open_date.replace(" ", "")
    open_date = open_date.split()[0]
    print('{} ({}) - {}'.format(title, percent, open_date))
    

# print(movieList)


