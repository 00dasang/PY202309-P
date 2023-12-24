import os
from PIL import Image, ImageTk
from tkinter import Tk, Label, Entry, Button, StringVar, filedialog, Canvas, Frame, Scrollbar

# 전역 변수로 root를 선언합니다.
root = None

image_list = []  
matching_images = []  
images_folder = ""
canvas = None  # canvas를 전역 변수로 초기화

def show_images_with_keyword(keyword):
    
    global matching_images, images_folder, canvas, scrollable_frame
  

    matching_images = [f for f in os.listdir(images_folder) if keyword.lower() in f.lower() and f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    
    # Canvas 내부에 배치하기 위한 프레임 생성
    scrollable_frame = Frame(canvas)
    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    for image_file in matching_images:
        img = Image.open(os.path.join(images_folder, image_file))
        img.thumbnail((1280, 720))

        img_tk = ImageTk.PhotoImage(img)
        image_list.append(img_tk)

        label = Label(scrollable_frame, image=img_tk, text=image_file, compound='top')
        label.image = img_tk
        label.pack(padx=5, pady=5)

def on_closing():
    for img_tk in image_list:
        img_tk.__del__()
    root.destroy()

def get_keyword_and_show_images(root):
    global matching_images, images_folder, canvas

    keyword = input("이미지 검색 키워드를 입력하세요: ")
    images_folder = "C:/Users/00das/Desktop/커밋프로젝트/PY202309-P/Sources/Project_codes/Road_Design_references"

    # Canvas 초기화
    if canvas:
        canvas.destroy()
    canvas = Canvas(root)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)

    show_images_with_keyword(keyword)

def get_root():
    global root
    return root

def main():
    global root
    root = Tk()
    root.title("Image Viewer with Keyword")

    keyword_var = StringVar()
    keyword_entry = Entry(root, textvariable=keyword_var, width=30)
    keyword_entry.pack(pady=10)

    show_button = Button(root, text="Show Images", command=get_keyword_and_show_images(root))
    show_button.pack(pady=10)

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()

if __name__ == "__main__":
    main()