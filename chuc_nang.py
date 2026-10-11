import tkinter as tk
from tkinter import messagebox
from kiem_tra import lay_du_lieu


def xoa_input(entries):
    for e in entries:
        e.delete(0, tk.END)


def them(table, entries):
    data = lay_du_lieu(entries)
    if data:
        table.insert("", "end", values=data)
        xoa_input(entries)


def sua(table, entries):
    selected = table.selection()
    if not selected:
        messagebox.showwarning("Lỗi", "Hãy chọn sinh viên cần sửa!")
        return
    data = lay_du_lieu(entries)
    if data:
        table.item(selected, values=data)
        xoa_input(entries)


def xoa(table, entries):
    selected = table.selection()
    if not selected:
        messagebox.showwarning("Lỗi", "Hãy chọn sinh viên cần xóa!")
        return
    table.delete(selected)
    xoa_input(entries)


def chon_sv(table, entries):
    """Bấm vào một dòng thì hiện dữ liệu lên các ô nhập."""
    selected = table.selection()
    if selected:
        xoa_input(entries)
        values = table.item(selected)["values"]
        for i in range(4):
            entries[i].insert(0, values[i])
