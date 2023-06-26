# urllib.request 를 이용한 요청 보내기

# urllib 는 표준아리브러리로 별도 설치 필요 없음
import urllib.request

# GET 요청
response = urllib.request.urlopen('http://www.naver.com')
print( type(response) )

# 응답 결과 확인 - read()
print( response.read(500) )











