import readlines
import sending_email
import finding_image
import keyword_recommendation
import tkinter as tk

def show_menu():
    print("1. 검색")
    print("2. 이메일 전송")
    print("3. 이미지 검색")
    print("4. 검색어 추천")  # 추가된 부분
    choice = input("원하는 기능의 번호를 선택하세요: ")
    return choice

def main():
    global root_for_image
    root_for_image = finding_image.get_root()
    if root_for_image is None:
        root_for_image = tk.Tk()
        finding_image.root = root_for_image

    while True:
        choice = show_menu()

        if choice == '1':
            readlines.main()
        elif choice == '2':
            sending_email.main()
        elif choice == '3':
            root_for_image.mainloop()
            root_for_image = finding_image.get_root()
            if root_for_image is None:
                finding_image.get_keyword_and_show_images()
                root_for_image = finding_image.get_root()
            root_for_image.mainloop()
        elif choice == '4':
            keyword_recommendation.extract_english_words()
            print("검색어 추천 기능입니다.")
        else:
            print("올바른 번호를 입력하세요.")

        again = input("다른 기능을 실행하시겠습니까? (y/n): ")
        if again.lower() != 'y':
            break

if __name__ == "__main__":
    main()