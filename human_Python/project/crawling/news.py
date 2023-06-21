# 웹 크롤링
# pip install requests
# pip install beautifulsoup4
# pip install lxml

# import : 모듈, 패키지를 포함하는 키워드
import requests
from bs4 import BeautifulSoup
           
# 'User-Agent' 헤더 추가 (사용자 정보)
# http://m.avalon.co.kr/check.html    <- 여기서 복사
headers = {
    'User-Agent' : ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'),
}
           
url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105"
html = requests.get(url, headers=headers)

print(html)


# html 분석
soup = BeautifulSoup(html.text, 'lxml')

# # 선택자로 지정해서 태그 가져오기
newsList = soup.select('.sh_item')

# 뉴스 제목
# 기사내용
# 신문사
# --------------
# 제목 (신문사) 
# : 기사내용
# --------------
for news in newsList:
    title = news.select('.sh_text_headline')[0].get_text()
    company = news.select('.sh_text_press')[0].get_text()
    content = news.select('.sh_text_lede')[0].get_text()
    
    print('----------------------------')
    print('{} ({})'.format(title, company))
    print(' : {}'.format(content))
    print('----------------------------')
    
    # 위의 형식으로 출력해보세요...
    # print(news)
   