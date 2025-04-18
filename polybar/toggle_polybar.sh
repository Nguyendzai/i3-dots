#!/bin/bash

# Kiểm tra xem Polybar có đang chạy không
if pgrep -x "polybar" > /dev/null; then
    # Nếu đang chạy, tắt tất cả các tiến trình Polybar
    pkill polybar
else
    # Nếu không chạy, khởi động lại Polybar (hoặc chạy lệnh khởi động của bạn)
    ~/.config/polybar/launch.sh  # Thay bằng lệnh start polybar của bạn
fi
