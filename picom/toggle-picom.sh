#!/bin/bash

if pgrep -x "picom" > /dev/null; then
    killall picom
    notify-send "🌫️ Picom" "Tắt picom"
else
    picom &
    notify-send "🌫️ Picom" "Bật picom"
fi
