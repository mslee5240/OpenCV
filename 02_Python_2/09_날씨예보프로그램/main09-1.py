# 1. 패키지 가져오기
import requests
import json

api_key = '58659c9f71f5c4b54841fc18d52d990a'  # https://openweathermap.org/api 날씨 안내 사이트 여기에 발급받은 API 키를 입력하세요.
city_name = 'seoul'

# 2. API 호출  
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
response = requests.get(url)

# 3. JSON 데이터 파싱
data = json.loads(response.text)

# 4. 날씨 정보 출력
print(f'{city_name}의 날씨: {data["weather"][0]["description"]}')
print(f'현재 온도: {data["main"]["temp"]}°C')
print(f'체감 온도: {data["main"]["feels_like"]}°C')
