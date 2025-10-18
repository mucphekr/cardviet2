#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script tao the sinh vien - Gemini AI Version
- Su dung Gemini API de tao ten sinh vien Viet Nam
- Quan ly ten da tao voi used_names.txt
- Tu chon so luong the muon tao
- Tu dong random ten sinh vien
"""

from PIL import Image, ImageDraw, ImageFont
import os
import sys
from gemini_service import generate_student_names
from config import X_RATIO, Y_RATIO, FONT_SIZE, TEMPLATE_PATH, OUTPUT_DIR, USED_NAMES_FILE

def generate_students(num_students):
    """Tao danh sach sinh vien su dung Gemini API"""
    print(f"Dang tao {num_students} ten sinh vien bang Gemini AI...")
    students = generate_student_names(num_students)
    print(f"Da tao thanh cong {len(students)} ten sinh vien")
    return students

def load_created_names():
    """Doc danh sach ten da tao tu used_names.txt"""
    created_names = set()
    
    if os.path.exists(USED_NAMES_FILE):
        try:
            with open(USED_NAMES_FILE, 'r', encoding='utf-8-sig') as file:
                for line in file:
                    name = line.strip()
                    if name:
                        created_names.add(name)
        except:
            pass
    
    return created_names

def save_created_names(names):
    """Luu danh sach ten da tao vao used_names.txt"""
    try:
        with open(USED_NAMES_FILE, 'a', encoding='utf-8-sig') as file:
            for name in names:
                file.write(f"{name}\n")
    except:
        pass

def add_name_to_card(template_path, student_name, output_path):
    """Dien ten sinh vien len anh"""
    try:
        # Mo anh template
        img = Image.open(template_path)
        draw = ImageDraw.Draw(img)
        
        # Chon font
        name_font = None
        font_paths = [
            "arial.ttf", 
            "times.ttf", 
            "calibri.ttf",
            r"C:\Windows\Fonts\arial.ttf",
            r"C:\Windows\Fonts\arialuni.ttf"
        ]
        
        for font_path in font_paths:
            try:
                name_font = ImageFont.truetype(font_path, FONT_SIZE)
                break
            except:
                continue
        
        if name_font is None:
            name_font = ImageFont.load_default()
        
        # Ve ten khong dam - ro rang hon
        text_color = (0, 0, 0)  # Mau den
        
        # Tinh toan vi tri tu ty le
        x_pos = int(img.width * X_RATIO)
        y_pos = int(img.height * Y_RATIO)
        
        # Chi ve text chinh - khong co hieu ung dam
        draw.text((x_pos, y_pos), student_name, 
                 fill=text_color, font=name_font)
        
        # Luu anh
        img.save(output_path)
        return True
        
    except Exception as e:
        return False

def get_number_of_cards():
    """Lay so luong the muon tao tu nguoi dung"""
    try:
        # Kiem tra tham so dong lenh
        if len(sys.argv) > 1:
            try:
                num = int(sys.argv[1])
                if num > 0:
                    return num
            except:
                pass
        
        # Neu khong co tham so, mac dinh tao 3 the
        return 3
        
    except:
        return 3

def main():
    """Ham chinh"""
    if not os.path.exists(TEMPLATE_PATH):
        print(f"Khong tim thay template: {TEMPLATE_PATH}")
        return
    
    # Lay so luong the muon tao
    num_cards = get_number_of_cards()
    print(f"Se tao {num_cards} the sinh vien")
    
    # Doc danh sach ten da tao
    created_names = load_created_names()
    print(f"Da co {len(created_names)} ten da su dung")
    
    # Tao danh sach sinh vien moi
    students = generate_students(num_cards)
    
    # Loc sinh vien chua co the (tránh trùng lặp)
    new_students = [name for name in students if name not in created_names]
    
    # Nếu có tên trùng, tạo thêm tên mới
    if len(new_students) < num_cards:
        needed = num_cards - len(new_students)
        print(f"Tao them {needed} ten de tranh trung lap...")
        additional_students = generate_students(needed * 2)  # Tạo nhiều hơn để chọn
        additional_new = [name for name in additional_students if name not in created_names]
        new_students.extend(additional_new[:needed])
    
    if not new_students:
        print("Khong the tao ten sinh vien moi")
        return
    
    # Chọn đúng số lượng cần thiết
    selected_students = new_students[:num_cards]
    
    # Tao thu muc output
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    success_count = 0
    created_this_time = []
    
    print(f"Bat dau tao the cho {len(selected_students)} sinh vien...")
    
    for i, name in enumerate(selected_students, 1):
        try:
            print(f"  {i}/{len(selected_students)}: {name}")
            # Tao ten file an toan
            safe_name = name.replace(' ', '_').replace('/', '_').replace('\\', '_')
            output_path = os.path.join(OUTPUT_DIR, f"card_{safe_name}.png")
            
            # Dien ten len the
            if add_name_to_card(TEMPLATE_PATH, name, output_path):
                success_count += 1
                created_this_time.append(name)
                print(f"    Thanh cong")
            else:
                print(f"    That bai")
                
        except Exception as e:
            print(f"    Loi: {e}")
    
    # Luu danh sach ten da tao
    if created_this_time:
        save_created_names(created_this_time)
        print(f"Da luu {len(created_this_time)} ten vao {USED_NAMES_FILE}")
    
    print(f"Hoan thanh! Da tao {success_count}/{len(selected_students)} the sinh vien")

if __name__ == "__main__":
    main()