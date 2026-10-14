# Khai báo giá trị mẫu (v1)
ma_quan_sat = "MQ01"
dai_luong = "Nhiệt độ"
gia_tri_do = 25.678
don_vi = "°C"
thoi_diem_text = "12:00 15/10/2026"

# In bản ghi kết quả hoàn chỉnh ra màn hình
print("\n--- BẢN GHI QUAN SÁT ---")
print(f"Mã quan sát : {ma_quan_sat}")
print(f"Đại lượng : {dai_luong}")
print(f"Giá trị : {gia_tri_do:.2f} {don_vi}")
print(f"Thời điểm : {thoi_diem_text}")
observer = input("Nhập người quan sát: ")
print(f"Người quan sát: {observer}")
