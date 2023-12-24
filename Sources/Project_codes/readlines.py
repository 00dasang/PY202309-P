import re
from collections import Counter

def load_file(filename):
    filename = filename.strip('"')
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def preprocess_text(text):
    sentences = re.split(r'[.!?]', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    return sentences

def compute_similarity(keyword, sentence):
    keyword_count = Counter(keyword.split())
    sentence_count = Counter(sentence.split())
    
    common_words = keyword_count & sentence_count
    total_keywords = sum(keyword_count.values())
    
    return sum(common_words.values()) / total_keywords if total_keywords else 0

def save_keyword(keyword):
    with open('keywords.txt', 'a+', encoding='utf-8') as file:
        file.seek(0)
        keywords = file.readlines()
        keywords = [k.strip() for k in keywords]
        
        if keyword in keywords:
            idx = keywords.index(keyword)
            count_line = keywords[idx + 1]
            count = int(count_line)
            keywords[idx + 1] = str(count + 1)  # 빈도수 업데이트
            file.seek(0)
            file.truncate()
            file.writelines([f"{k}\n" for k in keywords])
        else:
            file.write(keyword + '\n1\n')

def main():
    filename = input("파일 경로를 입력하세요: ")
    keyword = input("키워드를 입력하세요: ")
    
    save_keyword(keyword)
    
    text = load_file(filename)
    sentences = preprocess_text(text)
    
    similarities = [(compute_similarity(keyword, sentence), sentence) for sentence in sentences]
    sorted_sentences = sorted(similarities, key=lambda x: x[0], reverse=True)
    
    top_10_sentences = sorted_sentences[:10]
    
    for rank, (similarity, sentence) in enumerate(top_10_sentences, start=1):
        print(f"{rank}. {similarity:.2f}: {sentence}")

if __name__ == "__main__":
    main()