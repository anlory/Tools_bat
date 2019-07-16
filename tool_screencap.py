# adb shell screencap  -p  /sdcard/photo.png
# adb pull /sdcard/photo.png
# adb shell rm /sdcard/photo.png
# ping -n 5 127.0.0.1 > nul
import anlory

fileName = "/sdcard/screenShot_"+anlory.get_time()+".png"
cmd = "adb shell screencap -p " + fileName
anlory.exec_cmd(cmd)

cmd = "adb pull "+fileName
anlory.exec_cmd(cmd)


cmd = "adb shell rm "+fileName
anlory.exec_cmd(cmd)

anlory.short_pause()