
# 1. 패키지 가져오기
import random

# 2. 파일에서 단어 가져오는 함수
def load_words(filename):
    words = {}
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            word, meaning = line.strip().split(":")
            words[word] = meaning
    return words

# 3. 퀴즈 함수
def quiz(words):
    word_list = list(words.keys())
    random.shuffle(word_list)
    for word in word_list:
        meaning = words[word]
        answer = input(f"{word}의 뜻은 무엇일까요? ")
        if answer == meaning:
            print("정답입니다!")
        else:
            print(f"틀렸습니다. 정답은 {meaning}입니다.")

# 4. word_list.txt 파일 읽어서 퀴즈 진행하기
if __name__ == "__main__":
    filename = r"12_단어암기프로그램\word_list.txt"
    words = load_words(filename)
    quiz(words)
