adb shell screencap  -p  /sdcard/photo.png
adb pull /sdcard/photo.png
adb shell rm /sdcard/photo.png
ping -n 5 127.0.0.1 > nul