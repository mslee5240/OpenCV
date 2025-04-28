# 1. 패키지 가져오기
from gtts import gTTS

# 2. 각 문장을 리스트에 저장
sentences = ["안녕하세요", "반갑습니다", "오늘은 날씨가 좋네요"]

# 3. 문장별로 mp3 파일 생성
for i, sentence in enumerate(sentences):
    tts = gTTS(text=sentence, lang='ko')
    filename = str(i+1) + "번 " + sentence + ".mp3"
    tts.save('10_오디오파일재생프로그램\\' + filename)