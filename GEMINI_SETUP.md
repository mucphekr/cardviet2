# Hướng Dẫn Cấu Hình Gemini API

## 1. Lấy API Key từ Google AI Studio

1. Truy cập [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Đăng nhập bằng tài khoản Google
3. Click "Create API Key"
4. Copy API key được tạo

## 2. Cấu Hình API Key

Mở file `config.py` và thay thế:

```python
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY_HERE"
```

Thành:

```python
GEMINI_API_KEY = "your_actual_api_key_here"
```

## 3. Cài Đặt Dependencies

```bash
pip install google-generativeai
```

## 4. Test API

Chạy file test để kiểm tra API:

```bash
python gemini_service.py
```

## 5. Sử Dụng

### Command Line:
```bash
python app.py 5  # Tạo 5 thẻ sinh viên
```

### Web Interface:
1. Mở `index_gemini.html` trong trình duyệt
2. Upload template thẻ
3. Nhập số lượng thẻ muốn tạo
4. Click "Tạo Thẻ với AI"

## 6. Tính Năng

- ✅ Tự động tạo tên sinh viên Việt Nam bằng AI
- ✅ Tránh trùng lặp tên đã sử dụng
- ✅ Lưu trữ danh sách tên đã tạo
- ✅ Giao diện web thân thiện
- ✅ Tự động tạo script form điền thông tin

## 7. Cấu Trúc File

```
├── app.py                 # Script chính
├── gemini_service.py      # Service Gemini API
├── config.py              # Cấu hình
├── index_gemini.html      # Giao diện web
├── used_names.txt         # Danh sách tên đã sử dụng
└── student_cards/         # Thư mục chứa thẻ đã tạo
```

## 8. Troubleshooting

### Lỗi API Key:
- Kiểm tra API key có đúng không
- Đảm bảo API key có quyền truy cập Gemini

### Lỗi Network:
- Kiểm tra kết nối internet
- Thử lại sau vài phút

### Fallback Mode:
Nếu Gemini API không hoạt động, hệ thống sẽ tự động chuyển sang chế độ fallback sử dụng danh sách tên có sẵn.
