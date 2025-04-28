# Terminal 에서 pip install googletrans==4.0.0-rc1 실행하기
from googletrans import Translator

# 번역기 생성
translator = Translator()

# 번역할 파일 경로
input_file_path = r"02_번역프로그램\02_inputfile.txt"
# 번역된 파일 저장 경로
output_file_path = r"02_번역프로그램\02_outputfile.txt"


# 파일 읽기
with open(input_file_path, "r", encoding="utf-8") as input_file:
    text = input_file.read()

# 번역
result = translator.translate(text, dest="ko")

# 번역된 결과를 파일에 쓰기
with open(output_file_path, "w", encoding="utf-8") as output_file:
    output_file.write(result.text)
