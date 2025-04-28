# 1. 패키지 가져오기
import requests
import json
import datetime
import openpyxl
import time

api_key = '58659c9f71f5c4b54841fc18d52d990a'  # https://openweathermap.org/api 날씨 안내 사이트 여기에 발급받은 API 키를 입력하세요.
city_name = 'seoul'

# 2. 엑셀 파일 생성
wb = openpyxl.Workbook()
ws = wb.active
ws.append(['Date', 'Time', 'Weather', 'Temperature', 'Feels Like'])

# 3. API를 입력하여 날씨사이트 정보 호출하고 가져온 정보 저장한 다음 엑셀에 데이터 저장
while True:
    # API 호출
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
    response = requests.get(url)

    # JSON 데이터 파싱
    data = json.loads(response.text)

    # 날씨 정보 저장
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    weather = data['weather'][0]['description']
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']

    # 엑셀 파일에 데이터 추가
    ws.append([current_time.split()[0], current_time.split()[1], weather, temp, feels_like])
    wb.save(r'09_날씨예보프로그램\weather_data.xlsx')

    # 30분 대기
    time.sleep(1800)
