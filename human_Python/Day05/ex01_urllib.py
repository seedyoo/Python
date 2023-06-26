# urllib.request 를 이용한 요청 보내기

# urllib 는 표준라이브러리로 별도 설치 필요 없음
import urllib.request

# GET 요청
response = urllib.request.urlopen('http://www.naver.com')

print('-------------------------')
print('GET 요청하기')
print( type(response) )     # http.client.HTTPResponse 클래스

# 응답 상태 코드
print( response.status )

# 응답 결과 확인 
# - read( 바이트 수 )
#   응답 데이터를 디코딩하지 않고 읽어온다.
print( response.read(500) )
# decode() 함수로 utf-8 으로 디코딩
print( response.read(500).decode('utf-8') )


# ############################################################
# POST 요청
import urllib.request
data = { 
            'title' : '제목',
            'writer' : '김휴먼',
            'content' : '내용입니다...',
        }

# 데이터 인코딩
data = urllib.parse.urlencode(data).encode('utf-8')

url = 'http://192.168.0.200:8080/board/insert'
req = urllib.request.Request(url, data=data, method='POST')
res = urllib.request.urlopen(req)
result = res.read(100).decode('utf-8')
print('-------------------------')
print('POST 요청하기')
print(f'status : {res.status}')
print(f'result : {result}')


# POST 요청 - JSON
import urllib.request
import json
data = { 
            'title' : '제목',
            'writer' : '김휴먼',
            'content' : '내용입니다...',
        }

# 데이터 인코딩
# json.dumps() : 데이터를 JSON 문자열로 변환
json_data = json.dumps(data).encode('utf-8')
print(f'json_data : {json_data}')

url = 'http://192.168.0.200:8080/api/board'
req = urllib.request.Request(url, data=json_data, method='POST')
req.add_header('Content-Type', 'application/json')

res = urllib.request.urlopen(req)
result = res.read(100).decode('utf-8')
print('-------------------------')
print('JSON 데이터 POST 요청하기')
print(f'status : {res.status}')
print(f'result : {result}')


# PUT 요청 - JSON
import urllib.request
import json

url = 'http://192.168.0.200:8080/api/board'
data = { 
            'title' : '제목',
            'writer' : '김휴먼',
            'content' : '내용입니다...',
        }
data['boardNo'] = 2000
data['title'] = '수정 제목'
json_data = json.dumps(data).encode('utf-8')
req = urllib.request.Request(url, data=json_data, method='PUT')
req.add_header('Content-Type', 'application/json')

res = urllib.request.urlopen(req)
result = res.read(100).decode('utf-8')
print('-------------------------')
print('JSON 데이터 PUT 요청하기')
print(f'status : {res.status}')
print(f'result : {result}')


# DELETE 요청 - JSON
import urllib.request
import json

url = 'http://192.168.0.200:8080/api/board'
data = { 
            'boardNo' : 1000,
        }
json_data = json.dumps(data).encode('utf-8')
req = urllib.request.Request(url, data=json_data, method='DELETE')
req.add_header('Content-Type', 'application/json')

res = urllib.request.urlopen(req)
result = res.read(100).decode('utf-8')
print('-------------------------')
print('JSON 데이터 DELETE 요청하기')
print(f'status : {res.status}')
print(f'result : {result}')

