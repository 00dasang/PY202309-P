import re
from collections import Counter

def load_file(filename):
    # 파일 경로 주변의 따옴표 제거
    filename = filename.strip('"')
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def preprocess_text(text):
    # 문장으로 분리
    sentences = re.split(r'[.!?]', text)
    # 불필요한 공백 및 문장 제거
    sentences = [s.strip() for s in sentences if s.strip()]
    return sentences

def compute_similarity(keyword, sentence):
    keyword_count = Counter(keyword.split())
    sentence_count = Counter(sentence.split())
    
    # 단어 빈도수를 기반으로 키워드와 문장의 관련성 계산
    common_words = keyword_count & sentence_count
    total_keywords = sum(keyword_count.values())
    
    return sum(common_words.values()) / total_keywords if total_keywords else 0

def main():
    filename = input("파일 경로를 입력하세요: ")
    keyword = input("키워드를 입력하세요: ")
    
    text = load_file(filename)
    sentences = preprocess_text(text)
    
    # 문장과 키워드 간의 관련성 계산
    similarities = [(compute_similarity(keyword, sentence), sentence) for sentence in sentences]
    
    # 관련성이 높은 순서대로 문장 정렬
    sorted_sentences = sorted(similarities, key=lambda x: x[0], reverse=True)
    
    # 상위 10개 문장만 출력
    top_10_sentences = sorted_sentences[:10]
    
    # 결과 출력
    for rank, (similarity, sentence) in enumerate(top_10_sentences, start=1):
        print(f"{rank}. {similarity:.2f}: {sentence}")

if __name__ == "__main__":
    main()