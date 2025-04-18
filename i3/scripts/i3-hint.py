#!/usr/bin/env python3
import os
import subprocess
from pathlib import Path

config_path = Path.home() / ".config/i3/config"

if not config_path.exists():
    print("Không tìm thấy tệp cấu hình i3!")
    exit(1)

keybinds = []
last_comment = "(Không có chú thích)"  # Mặc định nếu không có chú thích

with open(config_path, "r") as f:
    for line in f:
        line = line.strip()
        # Kiểm tra nếu dòng là chú thích
        if line.startswith("#"):
            last_comment = line[1:].strip() or "(Không có chú thích)"  # Lưu chú thích, bỏ dấu #
        # Kiểm tra nếu dòng là bindsym
        elif line.startswith("bindsym"):
            parts = line.split("#", 1)  # Tách phần lệnh và chú thích inline (nếu có)
            command_part = parts[0].strip()
            tokens = command_part.split()
            key_combo = tokens[1] if len(tokens) > 1 else ""
            action = " ".join(tokens[2:]) if len(tokens) > 2 else ""
            # Sử dụng chú thích từ dòng trước (last_comment)
            keybinds.append(f"{key_combo:<20} ▶ {last_comment}")
            last_comment = "(Không có chú thích)"  # Reset chú thích sau khi sử dụng

if not keybinds:
    print("Không tìm thấy phím tắt nào.")
    exit(1)

# Hiển thị qua rofi
menu = "\n".join(keybinds)
subprocess.run(["rofi", "-dmenu", "-i", "-p", "i3 Keybinds"], input=menu, text=True)
