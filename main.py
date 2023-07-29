from tkinter import *
from tkinter import filedialog, font
from tkinter import messagebox
import tkinter as tk
import customtkinter
import os


FILE_PATH = ""
WIN_WIDTH = 1200
WIN_HEIGHT = 750
FONT_SIZE = 15
FONT_FAMILY = "Bahnschrift"
LABEL_FONT = ("Bahnschrift", 20)
DEFAULT_FONT = ("Bahnschrift", 15)
FONT_SIZE_LIST = [str(i) for i in range(1,257)]

def about_dev():
    messagebox.showinfo(title="About Devs", message="Made by @mahiru7229")

def font_family_callback(choice):
    global FONT_FAMILY
    global FONT_SIZE
    FONT_FAMILY = choice
    text_box.configure(font=(FONT_FAMILY,FONT_SIZE))

def font_size_callback(choice):
    global FONT_FAMILY
    global FONT_SIZE
    FONT_SIZE = int(choice)
    text_box.configure(font=(FONT_FAMILY,FONT_SIZE))

def submit_font_size():
    global FONT_FAMILY
    global FONT_SIZE
    try:
        FONT_SIZE = int(font_size.get())
        text_box.configure(font=(FONT_FAMILY,FONT_SIZE))
    except Exception:
        messagebox.showerror(title="Lỗi", message="Số không hợp lệ !")
    


def new_file():
    global FILE_PATH
    f = filedialog.asksaveasfilename(defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("Python", "*.py"), ("All files", "*.*")])
    if f:
        FILE_PATH = f
        open(f, "w", encoding="utf-8")
        windows.title(f"{os.path.basename(f)} - Text Editor 1.0")

def open_file():
    global FILE_PATH
    f = filedialog.askopenfilename(defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("Python", "*.py"), ("All files", "*.*")])
    if f:
        FILE_PATH = f
        try:
            with open(f, "r", encoding="utf-8") as a:
                text_box.delete("1.0", tk.END)
                text_box.insert("1.0",a.read())
                a.close()
            windows.title(f"{os.path.basename(f)} - Text Editor 1.0")
        except Exception:
            messagebox.showerror(title="Lỗi", message="Không thể mở file !")
        finally:
            a.close()
def save_file():
    global FILE_PATH
    if not FILE_PATH:
        f = filedialog.asksaveasfilename(defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("Python", "*.py"), ("All files", "*.*")])
        if f:
            FILE_PATH = f
            try:
                with open(f, "w", encoding="utf-8") as a:
                    a.write(text_box.get("1.0", tk.END))
                    a.close()
                windows.title(f"{os.path.basename(f)} - Text Editor 1.0")
            except Exception:
                messagebox.showerror(title="Lỗi", message="Không thể lưu file !")
            finally:
                a.close()
    else:
        try:
            with open(FILE_PATH, "w", encoding="utf-8") as a:
                a.write(text_box.get("1.0", tk.END))
                a.close()
        except Exception:
            messagebox.showerror(title="Lỗi", message="Không thể lưu file !")
        finally:
            a.close()
def save_file_as():
    f = filedialog.asksaveasfilename(defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("Python", "*.py"), ("All files", "*.*")])
    if f:
        try:
            with open(f, "w", encoding="utf-8") as a:
                a.write(text_box.get("1.0", tk.END))
                a.close()
            windows.title(f"{os.path.basename(f)} - Text Editor 1.0")
        except Exception:
            messagebox.showerror(title="Lỗi", message="Không thể lưu file !")
        finally:
            a.close()


customtkinter.set_appearance_mode("dark")







def toggle_status():
    if show_status.get():
        customtkinter.set_appearance_mode("dark")
    else:
        customtkinter.set_appearance_mode("light")

def get_line_column(event):
    cursor_index = text_box.index(tk.INSERT)
    line, column = map(int, cursor_index.split('.'))
    l_c_label.configure(text=f"Ln {line}, Col {column}")





windows = customtkinter.CTk()


inf_frame = customtkinter.CTkFrame(windows)
inf_frame.pack(side="bottom")

text_box = customtkinter.CTkTextbox(windows,height=WIN_HEIGHT, font=DEFAULT_FONT)
text_box.pack(padx=5, pady=5, fill=tk.BOTH)


l_c_label = customtkinter.CTkLabel(inf_frame, text="Ln 1, Col 0", font = LABEL_FONT)
l_c_label.grid(padx=5, pady=5, row = 0, column = 0)

font_family = customtkinter.CTkOptionMenu(inf_frame, values=list(font.families()), fg_color=["#afb0b3","#3d3e40"],text_color=["#000000","#FFFFFF"], font=LABEL_FONT, command=font_family_callback)
font_family.set("Bahnschrift")
font_family.grid(padx=5, pady=5, row = 0, column = 1)

font_size = customtkinter.CTkComboBox(inf_frame,values=FONT_SIZE_LIST,  font=LABEL_FONT, command=font_size_callback)
font_size.set(str(FONT_SIZE))
font_size.grid(padx=5, pady=5, row = 0, column = 2)


submit_size_btn = customtkinter.CTkButton(inf_frame, text="Submit font size", fg_color=["#afb0b3","#3d3e40"],text_color=["#000000","#FFFFFF"],  font=LABEL_FONT, command=submit_font_size)
submit_size_btn.grid(padx=5, pady=5, row = 0, column = 3)












show_status = BooleanVar()
show_status.set(True)

menubar = Menu(windows)
file_menu = Menu(menubar, tearoff=0)
edit_menu = Menu(menubar, tearoff=0)
about_menu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="File", menu=file_menu)
menubar.add_cascade(label="Edit", menu=edit_menu)
menubar.add_cascade(label="About", menu=about_menu)


file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open (Ctrl + O)", command=open_file)
file_menu.add_command(label="Save (Ctrl + S)", command=save_file)
file_menu.add_command(label="Save As (Ctrl + Shift + S)", command=save_file_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=windows.destroy)

# edit_menu.add_command(label="Cut", command=lambda event: cut_text())
# edit_menu.add_command(label="Copy", command=lambda event: copy_text())
# edit_menu.add_command(label="Paste", command=lambda : paste_text())
edit_menu.add_separator()
edit_menu.add_checkbutton(label="Dark Mode", variable=show_status, command=toggle_status)



about_menu.add_command(label="About Devs", command=about_dev)



text_box.bind("<KeyRelease>", get_line_column)



# phim tat
windows.bind("<Control-o>",lambda event: open_file())
windows.bind("<Control-s>", lambda event:save_file())
windows.bind("<Control-Shift-s>", lambda event:save_file_as())



windows.configure(menu=menubar)
windows.title("Text Editor 1.0")
windows.geometry('{}x{}'.format(WIN_WIDTH, WIN_HEIGHT))
windows.mainloop()