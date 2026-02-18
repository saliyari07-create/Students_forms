import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def save_data():
    name = entry_name.get()
    family = entry_family.get()
    major = entry_major.get()
    class_name = combo.get()

    if name == "" or family == "" or major == "" or class_name == "انتخاب کنید":
        messagebox.showerror("خطا", "لطفاً همه فیلدها را پر کنید")
        return

    with open("students.txt", "a", encoding="utf-8") as file:
        file.write(f"{name},{family},{major},{class_name}\n")

    messagebox.showinfo("موفق", "اطلاعات ذخیره شد")

    entry_name.delete(0, tk.END)
    entry_family.delete(0, tk.END)
    entry_major.delete(0, tk.END)
    combo.set("انتخاب کنید")


# ساخت پنجره اصلی
window = tk.Tk()
window.title("فرم اطلاعات دانش‌آموز")
window.geometry("350x300")

class_list = ['Python', 'Java', 'HTML', 'CSS', 'C++']

tk.Label(window, text="نام").pack()
entry_name = tk.Entry(window)
entry_name.pack()

tk.Label(window, text="نام خانوادگی").pack()
entry_family = tk.Entry(window)
entry_family.pack()

tk.Label(window, text="رشته").pack()
entry_major = tk.Entry(window)
entry_major.pack()

tk.Label(window, text="نام کلاس").pack()
combo = ttk.Combobox(window, values=class_list, state="readonly")
combo.pack()
combo.set("انتخاب کنید")

tk.Button(window, text="ذخیره اطلاعات", command=save_data).pack(pady=15)

window.mainloop()