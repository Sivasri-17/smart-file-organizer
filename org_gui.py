import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# File categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"]
}

def organize_files():
    path = folder_path.get()
    
    if not path:
        messagebox.showwarning("Warning", "Please select a folder")
        return

    moved_files = 0

    files = os.listdir(path)

    for file in files:
        file_path = os.path.join(path, file)

        if os.path.isfile(file_path):
            for folder, extensions in file_types.items():
                if file.lower().endswith(tuple(extensions)):

                    folder_path_new = os.path.join(path, folder)

                    if not os.path.exists(folder_path_new):
                        os.makedirs(folder_path_new)

                    shutil.move(file_path, os.path.join(folder_path_new, file))
                    moved_files += 1
                    break

    result_label.config(text=f"Files organized: {moved_files}")

def browse_folder():
    folder_selected = filedialog.askdirectory()
    folder_path.set(folder_selected)

# GUI Window
root = tk.Tk()
root.title("Smart File Organizer")
root.geometry("400x250")

folder_path = tk.StringVar()

title = tk.Label(root, text="Smart File Organizer", font=("Arial", 16))
title.pack(pady=10)

entry = tk.Entry(root, textvariable=folder_path, width=40)
entry.pack(pady=5)

browse_btn = tk.Button(root, text="Browse Folder", command=browse_folder)
browse_btn.pack(pady=5)

organize_btn = tk.Button(root, text="Organize Files", command=organize_files)
organize_btn.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()