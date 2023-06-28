import urllib.request
from bs4 import BeautifulSoup


# 영화정보 가져오기
def getSearchList():
    url = 'https://www.signal.bz'
    res = urllib.request.urlopen(url)
    result = res.read().decode('utf-8')

    bs = BeautifulSoup( result, 'html.parser' )

    titles = bs.select('#app > div > main > div > section > div > section > section:nth-child(2) > div:nth-child(2) > div > div:nth-child(1) > div:nth-child(1) > a > span.rank-text')
    nums = bs.select('#app > div > main > div > section > div > section > section:nth-child(2) > div:nth-child(2) > div > div:nth-child(1) > div:nth-child(1) > a > span.rank-num')
    # rates = bs.select('.txt_append > .info_txt > .txt_num')
    # open_dates = bs.select('.txt_info > .txt_num')

    search_titles = []
    search_nums = []
    # movie_rates = []
    # movie_open_dates = []

    for item in titles:
        search_titles.append( item.text )
        # print(item.text)
    for item in nums:
        search_nums.append( item.text )
        # print(item.text)
    # for item in rates:
    #     movie_rates.append( item.text )
    #     # print(item.text)
    # for item in open_dates:
    #     movie_open_dates.append( item.text )
        # print(item.text)
        
        
    # count = len(movie_titles)

    # for i in range(count):
    #     print('#################################')
    #     print('영화 제목 :', movie_titles[i])
    #     print('평점 :', movie_points[i])
    #     print('예매율 :', movie_rates[i])
    #     print('개봉일 :', movie_open_dates[i])
    
    # 제목, 평점, 예매율, 개봉일
    result = (search_nums, search_titles)
    return result


###
