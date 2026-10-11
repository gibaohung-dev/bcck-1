from tkinter import messagebox

def lay_du_lieu(entries):
    """Lấy dữ liệu từ ô nhập, sai thì báo lỗi và trả về None."""
    ma = entries[0].get()
    ten = entries[1].get()
    try:
        tuoi = int(entries[2].get())
        diem = float(entries[3].get())
    except ValueError:
        messagebox.showwarning("Lỗi", "Tuổi và Điểm phải là số!")
        return None
    if ma == "" or ten == "":
        messagebox.showwarning("Lỗi", "Vui lòng nhập Mã số SV và Họ tên!")
        return None
    if diem < 0 or diem > 100:
        messagebox.showwarning("Lỗi", "Điểm rèn luyện phải từ 0 đến 100!")
        return None
    return (ma, ten, tuoi, diem)
