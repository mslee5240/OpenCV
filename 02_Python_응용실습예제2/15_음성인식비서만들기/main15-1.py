# 0. 패키지 설치하기 
# [terminal ] pip install pyaudio

# 1. 패키지 가져오기
import speech_recognition as sr

# 2. 마이크에서 음성 받아오기
r = sr.Recognizer()
with sr.Microphone() as source:
    print("말씀해주세요.")
    audio = r.listen(source)

# 3. 인식된 음성에서 텍스트 추출하기
text = r.recognize_google(audio, language='ko-KR')

print(text)
