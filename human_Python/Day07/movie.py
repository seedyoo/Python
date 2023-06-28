import urllib.request
from bs4 import BeautifulSoup

# 영화정보 가져오기
def getMovieList():
    url = 'https://movie.daum.net/ranking/reservation'
    res = urllib.request.urlopen(url)
    result = res.read().decode('utf-8')

    bs = BeautifulSoup( result, 'html.parser' )

    # select() 함수로 영화 제목, 평점, 예매율, 개봉일 가져오기
    titles = bs.select('.tit_item > .link_txt')
    points = bs.select('.txt_append > .info_txt > .txt_grade')
    rates = bs.select('.txt_append > .info_txt > .txt_num')
    open_dates = bs.select('.txt_info > .txt_num')

    movie_titles = []
    movie_points = []
    movie_rates = []
    movie_open_dates = []

    for item in titles:
        movie_titles.append( item.text )
        # print(item.text)
    for item in points:
        movie_points.append( item.text )
        # print(item.text)
    for item in rates:
        movie_rates.append( item.text )
        # print(item.text)
    for item in open_dates:
        movie_open_dates.append( item.text )
        # print(item.text)
        
    # count = len(movie_titles)
    # for i in range(count):
    #     print('#################################')
    #     print('영화 제목 :', movie_titles[i])
    #     print('평점 :', movie_points[i])
    #     print('예매율 :', movie_rates[i])
    #     print('개봉일 :', movie_open_dates[i])
    
    # 제목, 평점, 예매율, 개봉일 
    result = (movie_titles, movie_points, movie_rates, movie_open_dates)
    return result