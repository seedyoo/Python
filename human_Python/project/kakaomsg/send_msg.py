import json
import requests

# access_token 
access_token = '6a6iSsAi-YaIHaxY0XPOuT7T8kqZECbqXILSKzfmCj1ylwAAAYjiI5z6'

url = 'https://kapi.kakao.com/v2/api/talk/memo/default/send'

# header 정보
headers = {
    'Authorization' : 'Bearer ' + access_token
}

# 요청 정보
temp = {
            "object_type": "text",
            "text": input('메시지 : '),
            "link": {
                "web_url": "https://www.youtube.com",
                "mobile_web_url": "https://www.youtube.com"
            },
            # "button_title": "바로 확인"
        }

data = {
    'template_object' : json.dumps( temp )      # 파이썬 객체를 JSON 문자열로 직렬화하는 함수
}

# 나에게 카카오 메시지 보내기
response = requests.post(url, headers=headers, data=data)
print(response.status_code)

