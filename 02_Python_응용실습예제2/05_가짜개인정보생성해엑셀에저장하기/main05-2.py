# 1. 필요한 패키지 가져오기
from faker import Faker
from openpyxl import Workbook

fake = Faker('ko_KR')

# 2. 엑셀 파일 생성
wb = Workbook()
ws = wb.active

# 3. 헤더 추가
ws.append(['이름', '성별', '이메일', '전화번호'])

# 4. 가짜 데이터 생성 및 저장
for i in range(1000):
    name = fake.name()
    gender = fake.random_element(elements=('남', '여'))
    email = fake.email()
    phone_number = fake.phone_number()
    # ws 에 name, gender, email, phone_number 추가하기
    # code here

# 5. 엑셀 파일 저장 - 'personal_info.xlsx'로 저장하기
# code here
