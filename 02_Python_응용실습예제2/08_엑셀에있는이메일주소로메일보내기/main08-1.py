# 설치 안내 
# 0. openpyxl이 설치되지 않은 경우(엑셀에 데이터 저장하려면) - Terminal : pip install openpyxl

# 1. 필요한 라이브러리 가져오기 (openpyxl)
import openpyxl

# 2. 엑셀 파일 열기
wb = openpyxl.load_workbook('08_엑셀에있는이메일주소로메일보내기\email_list.xlsx')
sheet = wb.active

# 3. 각 행의 이메일과 이름 출력
for row in sheet.iter_rows(min_row=2, values_only=True):  # 첫 번째 행은 제외
    email, name = row
    print(f"{email}, {name}")

# 4. 엑셀 파일 닫기
wb.close()
