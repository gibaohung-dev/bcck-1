import tkinter as tk
from tkinter import ttk
from config import FIELDS
from chuc_nang import them, sua, xoa, chon_sv
window = tk.Tk()
window.title("TRANG QUẢN LÝ ĐIỂM RÈN LUYỆN SINH VIÊN")
window.geometry("700x450")
tk.Label(window, text="TRANG QUẢN LÝ ĐIỂM RÈN LUYỆN SINH VIÊN",
        font=("Arial", 20, "bold")).pack(pady=20)
# Các ô nhập
frame = tk.Frame(window)
frame.pack()
entries = []
for i in range(4):
    tk.Label(frame, text=FIELDS[i]).grid(row=i // 2, column=(i % 2) * 2, padx=5, pady=5)
entry = tk.Entry(frame)
entry.grid(row=i // 2, column=(i % 2) * 2 + 1, padx=5)
entries.append(entry)
# Bảng danh sách
table = ttk.Treeview(window, columns=FIELDS, show="headings")
for name in FIELDS:
        table.heading(name, text=name)
        table.column(name, width=130)
table.pack(pady=10, padx=20, fill="both", expand=True)
table.bind("<<TreeviewSelect>>", lambda event: chon_sv(table, entries))
# Các nút
button_frame = tk.Frame(window)
button_frame.pack(pady=15)
tk.Button(button_frame, text="Thêm sinh viên", width=12,
        command=lambda: them(table, entries)).pack(side="left", padx=5)
tk.Button(button_frame, text="Sửa thông tin", width=12,
        command=lambda: sua(table, entries)).pack(side="left", padx=5)
tk.Button(button_frame, text="Xóa sinh viên", width=12,
        command=lambda: xoa(table, entries)).pack(side="left", padx=5)
window.mainloop()