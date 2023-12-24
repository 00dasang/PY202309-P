import re

def extract_english_words(filename="keywords.txt"):
    try:
        with open(filename, 'r') as file:
            content = file.read()

        # 정규 표현식을 사용하여 영어 단어만 추출
        english_words = re.findall(r'\b[A-Za-z]+\b', content)

        # 중복 제거 및 정렬
        unique_words = sorted(set(english_words))

        for word in unique_words:
            print(word)

    except FileNotFoundError:
        print(f"{filename} 파일이 존재하지 않습니다.")

if __name__ == "__main__":
    extract_english_words()