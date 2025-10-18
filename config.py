#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cấu hình cho ứng dụng tạo thẻ sinh viên
"""

# Gemini API Configuration
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY_HERE"  # Thay thế bằng API key thực tế

# Cấu hình vị trí text trên thẻ (sử dụng tỷ lệ thay vì tọa độ tuyệt đối)
X_RATIO = 0.50    # Tỷ lệ ngang (0-1): 0.50 = 50% từ trái sang phải
Y_RATIO = 0.445   # Tỷ lệ dọc (0-1): 0.445 = 44.5% từ trên xuống dưới
FONT_SIZE = 32    # Kích thước font

# Tọa độ tuyệt đối (để tương thích với code cũ)
X_POSITION = 470  # Vị trí ngang (từ trái sang phải) - sẽ được tính từ tỷ lệ
Y_POSITION = 335  # Vị trí dọc (từ trên xuống dưới) - sẽ được tính từ tỷ lệ

# Cấu hình file
TEMPLATE_PATH = "Temp.png"
OUTPUT_DIR = "student_cards"
USED_NAMES_FILE = "used_names.txt"

# Cấu hình Gemini prompt
GEMINI_PROMPT = """
Bạn là một chuyên gia tạo tên sinh viên Việt Nam. Hãy tạo {num_names} tên sinh viên Việt Nam hoàn chỉnh (họ + tên đệm + tên).

Yêu cầu:
1. Tên phải là tên Việt Nam thực tế, phổ biến
2. Bao gồm cả họ và tên đệm
3. Tên phải có ý nghĩa tích cực
4. Tránh tên quá dài hoặc khó đọc
5. Mỗi tên trên một dòng riêng
6. Không có ký tự đặc biệt ngoài dấu tiếng Việt

Ví dụ:
Nguyễn Văn An
Trần Thị Bình
Lê Hoàng Minh
Phạm Thu Hương
"""

# Cấu hình fallback names (nếu Gemini API không hoạt động)
FALLBACK_NAMES = [
    "Nguyễn Văn An", "Trần Thị Bình", "Lê Hoàng Minh", "Phạm Thu Hương",
    "Hoàng Văn Đức", "Vũ Thị Lan", "Đặng Minh Tuấn", "Bùi Thị Mai",
    "Phan Văn Hùng", "Lý Thị Nga", "Tạ Minh Khang", "Đỗ Thị Linh",
    "Cao Văn Tuấn", "Ngô Thị Hoa", "Đinh Minh Đức", "Võ Thị Thu",
    "Trương Văn Nam", "Hồ Thị Lan", "Đào Minh Tuấn", "Lê Thị Hương"
]
