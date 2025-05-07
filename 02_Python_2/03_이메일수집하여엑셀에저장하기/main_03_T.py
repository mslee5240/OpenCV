
# 설치 안내 
# 1. requests 설치되지 않은 경우 - [Terminal] pip install requests 실행하기
# 2. BeautifulSoup 설치되지 않은 경우 - [Terminal] pip install BeautifulSoup4 실행하기
# 3. pandas 가 설치되지 않은 경우 - [Terminal] pip install pandas 
# 4. 엑셀관련 오류발생시 - [Terminal] pip install openpyxl

''' 웹페이지 내에 있는 이메일 주소 찾아서 파일에 저장하는 프로그램 
    1. 필요한 라이브러리 가져오기 (requests, BeautifulSoup, re , pandas)
    2. 웹페이지 요청하기 - url = "https://v.daum.net/v/20230303140011566" or 네이버 뉴스 중 다른 url 사용해도 됨  
    3. html 파서를 사용하여 웹페이지 가져오기
    4. 이메일을 찾기위한 정규식 패턴 지정하기 
    5. 웹 페이지에서 모든 텍스트 추출하기
    6. 이메일 패턴 매칭 후 리스트에 추가하기
    7. 같은 이메일이 있는 경우 중복 제거
    8. 이메일을 엑셀 파일로 저장
'''
'''
   이메일 주소를 검사하는 정규식 패턴입니다. 
   1. `r'...'`: `r`은 raw string 리터럴을 나타냅니다. 이를 사용하면 백슬래시를 특수 문자로 처리하는 것을 방지할 수 있습니다. 
   2. `\b`: 단어의 경계를 나타냅니다. 이메일 주소가 단어로 인식되고, 다른 문자열 내부에 포함되지 않도록 합니다.  
   3. `[A-Za-z0-9._%+-]+`: 이메일 주소의 사용자 이름 부분을 나타냅니다. 
      - `A-Za-z0-9`: 알파벳 대소문자와 숫자
      - `._%+-`: 이메일 주소에서 허용되는 특수 문자들
      - `+`: 앞의 문자나 그룹이 한 번 이상 반복될 수 있음을 나타냅니다.  
   4. `@`: '@' 문자입니다. 이메일 주소의 일부입니다.  
   5. `[A-Za-z0-9.-]+`: 도메인 이름 부분을 나타냅니다.
      - `A-Za-z0-9`: 알파벳 대소문자와 숫자
      - `.-`: 도메인에서 허용되는 특수 문자들
      - `+`: 앞의 문자나 그룹이 한 번 이상 반복될 수 있음을 나타냅니다.  
   6. `\.`: '.' 문자입니다. 도메인의 일부입니다.  
   7. `[A-Z|a-z]{2,}`: 최상위 도메인(TLD)을 나타냅니다. 예를 들어, `.com`, `.net`, `.org` 등입니다.
      - `A-Z|a-z`: 알파벳 대소문자
      - `{2,}`: 앞의 문자나 그룹이 최소 2회 이상 반복될 수 있음을 나타냅니다. (TLD는 대게 최소 두 글자입니다)  
   8. `\b`: 단어의 경계를 나타냅니다.
'''
# 1. 필요한 라이브러리 가져오기
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

# 2. 웹페이지 요청하기
url = "https://v.daum.net/v/20230303140011566"  # 이메일을 수집할 웹 페이지 주소 
response = requests.get(url)  # 웹 페이지 요청

# 3. html 파서를 사용하여 웹페이지 가져오기
soup = BeautifulSoup(response.text, "html.parser")  # BeautifulSoup 객체 생성
emails = []

# 4. 이메일을 찾기위한 정규식 패턴 지정하기 
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# 5. 웹 페이지에서 모든 텍스트 추출
text = soup.get_text()

# 6. 이메일 패턴 매칭 후 리스트에 추가
for match in re.findall(email_pattern, text):
    emails.append(match)

# 7. 같은 이메일이 있는 경우 중복 제거
emails = list(set(emails))

# 결과 출력
print(emails)

# 8. 이메일을 엑셀 파일로 저장
# 리스트로 저장한 이메일 주소 목록을 저장한 emails 를 판단스의 DataFrame으로 생성하여 저장하기 - 컬럼명 : Email
df = pd.DataFrame(emails, columns=["Email"])
# df를 엑셀로 저장하기 : 03_emalilist.xlsx 
df.to_excel("./03_emaillist.xlsx", index=False)