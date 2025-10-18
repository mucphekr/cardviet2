#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Service để tạo tên sinh viên Việt Nam sử dụng Gemini API
"""

import google.generativeai as genai
import random
from config import GEMINI_API_KEY, GEMINI_PROMPT, FALLBACK_NAMES

class GeminiNameGenerator:
    def __init__(self):
        """Khởi tạo Gemini API"""
        self.api_key = GEMINI_API_KEY
        self.model = None
        self._setup_gemini()
    
    def _setup_gemini(self):
        """Thiết lập Gemini API"""
        try:
            if self.api_key and self.api_key != "YOUR_GEMINI_API_KEY_HERE":
                genai.configure(api_key=self.api_key)
                self.model = genai.GenerativeModel('gemini-pro')
                print("OK: Gemini API configured successfully")
            else:
                print("WARNING: Gemini API key not configured, using fallback list")
                self.model = None
        except Exception as e:
            print(f"ERROR: Gemini API configuration error: {e}")
            self.model = None
    
    def generate_vietnamese_names(self, num_names):
        """
        Tạo danh sách tên sinh viên Việt Nam
        
        Args:
            num_names (int): Số lượng tên cần tạo
            
        Returns:
            list: Danh sách tên sinh viên
        """
        try:
            if self.model:
                return self._generate_with_gemini(num_names)
            else:
                return self._generate_with_fallback(num_names)
        except Exception as e:
            print(f"ERROR: Name generation error: {e}")
            return self._generate_with_fallback(num_names)
    
    def _generate_with_gemini(self, num_names):
        """Tạo tên sử dụng Gemini API"""
        try:
            prompt = GEMINI_PROMPT.format(num_names=num_names)
            response = self.model.generate_content(prompt)
            
            if response and response.text:
                # Xử lý response từ Gemini
                names = []
                lines = response.text.strip().split('\n')
                
                for line in lines:
                    name = line.strip()
                    # Kiểm tra tên hợp lệ
                    if name and self._is_valid_vietnamese_name(name):
                        names.append(name)
                
                # Nếu không đủ tên, bổ sung từ fallback
                if len(names) < num_names:
                    needed = num_names - len(names)
                    fallback_names = self._generate_with_fallback(needed)
                    names.extend(fallback_names)
                
                return names[:num_names]
            else:
                print("WARNING: Gemini API returned no results, using fallback")
                return self._generate_with_fallback(num_names)
                
        except Exception as e:
            print(f"ERROR: Gemini API error: {e}")
            return self._generate_with_fallback(num_names)
    
    def _generate_with_fallback(self, num_names):
        """Tạo tên sử dụng danh sách fallback"""
        print("Using fallback name list")
        
        # Tạo danh sách tên từ fallback names
        names = []
        for _ in range(num_names):
            # Kết hợp ngẫu nhiên họ và tên
            ho = random.choice([
                "Nguyễn", "Trần", "Lê", "Phạm", "Hoàng", "Vũ", "Đặng", "Bùi", 
                "Phan", "Lý", "Tạ", "Đỗ", "Cao", "Ngô", "Đinh", "Võ", "Trương"
            ])
            
            ten_dem = random.choice([
                "Văn", "Thị", "Hoàng", "Minh", "Thu", "Đức", "Thành", "Hùng",
                "Lan", "Mai", "Tuấn", "Hương", "Nam", "Linh", "Đức", "Thu"
            ])
            
            ten = random.choice([
                "An", "Bình", "Minh", "Hương", "Đức", "Lan", "Tuấn", "Mai",
                "Hùng", "Nga", "Khang", "Linh", "Nam", "Hoa", "Đức", "Thu"
            ])
            
            full_name = f"{ho} {ten_dem} {ten}"
            names.append(full_name)
        
        return names
    
    def _is_valid_vietnamese_name(self, name):
        """Kiểm tra tên có hợp lệ không"""
        if not name or len(name.strip()) < 3:
            return False
        
        # Kiểm tra có chứa ký tự tiếng Việt
        vietnamese_chars = "àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđ"
        has_vietnamese = any(char in vietnamese_chars for char in name.lower())
        
        # Kiểm tra có ít nhất 2 từ (họ + tên)
        words = name.strip().split()
        if len(words) < 2:
            return False
        
        return True

# Hàm tiện ích để sử dụng
def generate_student_names(num_names):
    """
    Hàm tiện ích để tạo tên sinh viên
    
    Args:
        num_names (int): Số lượng tên cần tạo
        
    Returns:
        list: Danh sách tên sinh viên
    """
    generator = GeminiNameGenerator()
    return generator.generate_vietnamese_names(num_names)

if __name__ == "__main__":
    # Test function
    print("Testing student name generation...")
    names = generate_student_names(5)
    print(f"Generated {len(names)} names:")
    for i, name in enumerate(names, 1):
        print(f"  {i}. {name}")
