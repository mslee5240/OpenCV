# faker 모듈 설치하기 : 터미널에서 pip install faker
# https://faker.readthedocs.io/en/master/

# 1. faker 모듈 가져오기
from faker import Faker

# 2. Faker 객체 생성하기 - 한국어 가짜 데이터 생성
fake = # code here  

# 3-1. 가짜 이름 생성
name = fake.name()

# 3-2. 가짜 주소 생성
address = # code here

# 3-3. 가짜 전화번호 생성
phone_number = fake.phone_number()

# 3-4. 가짜 이메일 주소 생성
email = fake.email()

# 3-5. 가짜 생년월일 생성
birthdate = fake.date_of_birth()

# 4. 결과 출력하기
print(name, address, phone_number, email, birthdate)
