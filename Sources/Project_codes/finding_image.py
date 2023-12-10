import os
from PIL import Image, ImageTk
from tkinter import Tk, Label, Entry, Button, StringVar, filedialog

# Keeping Tkinter PhotoImage
image_list = []  # 이미지를 저장할 리스트
matching_images = []  # 검색된 이미지를 저장할 리스트
images_folder = ""  # 이미지 폴더 경로를 저장할 변수

def show_images_with_keyword(keyword):
    global matching_images, images_folder  # 전역 변수로 선언

    # ... (이전 코드)

    for image_file in matching_images:
        img = Image.open(os.path.join(images_folder, image_file))
        img.thumbnail((1280, 720))

        img_tk = ImageTk.PhotoImage(img)
        image_list.append(img_tk)  # 리스트에 PhotoImage 추가

        label = Label(root, image=img_tk, text=image_file, compound='top')
        label.image = img_tk
        label.pack(padx=5, pady=5)

# Delete the PhotoImage when Tkinter root window close
def on_closing():
    # 이미지 삭제
    for img_tk in image_list:
        img_tk.__del__()

    root.destroy()

# 함수 추가
def get_keyword_and_show_images():
    global matching_images, images_folder  # 전역 변수로 선언
    keyword = keyword_var.get()
    images_folder = "C:/Users/00das/Desktop/커밋프로젝트/PY202309-P/Sources/Project_codes/Tunnel_excavation_method_images"
    matching_images = [f for f in os.listdir(images_folder) if keyword.lower() in f.lower() and f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    show_images_with_keyword(keyword)

# generate the window of Tkinter
root = Tk()
root.title("Image Viewer with Keyword")

# Create Entry Widgets to Enter Keywords
keyword_var = StringVar()
keyword_entry = Entry(root, textvariable=keyword_var, width=30)
keyword_entry.pack(pady=10)

# generate the button "Show Images"
show_button = Button(root, text="Show Images", command=get_keyword_and_show_images)
show_button.pack(pady=10)

# Protocol for handling window close event
root.protocol("WM_DELETE_WINDOW", on_closing)

# Start the Tkinter's main loop
root.mainloop()