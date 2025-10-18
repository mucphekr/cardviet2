# 🎓 Tạo Thẻ Sinh Viên với Gemini AI

Hệ thống tự động tạo thẻ sinh viên sử dụng Gemini AI để tạo tên sinh viên Việt Nam.

## ✨ Tính Năng

- 🤖 **Gemini AI Integration**: Sử dụng AI để tạo tên sinh viên Việt Nam tự động
- 🎯 **Tùy chọn số lượng**: Nhập số thẻ muốn tạo thay vì chọn từng tên
- 🔄 **Tránh trùng lặp**: Tự động lưu trữ tên đã sử dụng
- 🌐 **Giao diện web**: Giao diện thân thiện với người dùng
- 📱 **Responsive**: Hoạt động tốt trên mọi thiết bị

## 🚀 Cài Đặt

### 1. Cài đặt dependencies

```bash
pip install google-generativeai pillow
```

### 2. Cấu hình Gemini API

1. Truy cập [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Tạo API key
3. Cập nhật file `config.py`:

```python
GEMINI_API_KEY = "your_actual_api_key_here"
```

## 📁 Cấu Trúc File

```
├── app.py                 # Script chính
├── gemini_service.py      # Service Gemini API
├── config.py              # Cấu hình
├── index_gemini.html      # Giao diện web mới
├── index.html             # Giao diện web cũ
├── used_names.txt         # Danh sách tên đã sử dụng
├── student_cards/         # Thư mục chứa thẻ đã tạo
└── Temp.png              # Template thẻ
```

## 🎮 Sử Dụng

### Command Line

```bash
# Tạo 5 thẻ sinh viên
python app.py 5

# Tạo 10 thẻ sinh viên
python app.py 10
```

### Web Interface

1. Mở `index_gemini.html` trong trình duyệt
2. Upload template thẻ (Temp.png)
3. Nhập số lượng thẻ muốn tạo
4. Click "Tạo Thẻ với AI"

## 🔧 Cấu Hình

### Vị trí text trên thẻ

Chỉnh sửa trong `config.py`:

```python
X_POSITION = 470  # Vị trí ngang
Y_POSITION = 335  # Vị trí dọc
FONT_SIZE = 24    # Kích thước font
```

### Gemini API Prompt

Tùy chỉnh prompt trong `config.py`:

```python
GEMINI_PROMPT = """
Bạn là một chuyên gia tạo tên sinh viên Việt Nam...
"""
```

## 🧪 Test

```bash
# Test hệ thống
python simple_test.py

# Test đầy đủ
python test_gemini.py
```

## 📊 Tính Năng Nâng Cao

### 1. Tránh Trùng Lặp

- Tự động lưu tên đã sử dụng vào `used_names.txt`
- Kiểm tra trùng lặp trước khi tạo tên mới
- Tự động tạo thêm tên nếu cần

### 2. Fallback Mode

- Nếu Gemini API không hoạt động, tự động chuyển sang chế độ fallback
- Sử dụng danh sách tên có sẵn
- Đảm bảo hệ thống luôn hoạt động

### 3. Giao Diện Web

- Upload template trực tiếp
- Cấu hình vị trí text
- Xem trước thẻ đã tạo
- Download thẻ cá nhân
- Tạo script form tự động điền

## 🐛 Troubleshooting

### Lỗi Encoding

Nếu gặp lỗi encoding trên Windows:

```bash
# Chạy với encoding UTF-8
python -X utf8 app.py 5
```

### Lỗi Gemini API

1. Kiểm tra API key
2. Kiểm tra kết nối internet
3. Hệ thống sẽ tự động chuyển sang fallback mode

### Lỗi Template

- Đảm bảo file `Temp.png` tồn tại
- Kiểm tra quyền ghi file
- Đảm bảo thư mục `student_cards` có thể tạo

## 📈 Thống Kê

Hệ thống tự động theo dõi:
- Tổng số thẻ đã tạo
- Số tên đã sử dụng
- Số tên được tạo bởi AI

## 🔄 Cập Nhật

### Reset danh sách tên

```bash
# Xóa file used_names.txt để reset
rm used_names.txt
```

### Cập nhật cấu hình

Chỉnh sửa file `config.py` và restart ứng dụng.

## 📞 Hỗ Trợ

Nếu gặp vấn đề:

1. Kiểm tra log lỗi
2. Chạy test để kiểm tra hệ thống
3. Kiểm tra cấu hình API key
4. Đảm bảo template file tồn tại

## 🎯 Roadmap

- [ ] Hỗ trợ nhiều template
- [ ] Tự động detect vị trí text
- [ ] Batch processing
- [ ] API endpoint
- [ ] Database integration

---

**Lưu ý**: Để sử dụng đầy đủ tính năng AI, cần cấu hình Gemini API key. Hệ thống sẽ hoạt động ở chế độ fallback nếu không có API key.
