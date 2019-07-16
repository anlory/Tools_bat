import anlory
import time

cmd = "adb root"
anlory.exec_cmd(cmd)

cmd = "adb shell settings put system show_touches 1"
anlory.exec_cmd(cmd)

cmd = "adb shell settings put system pointer_location 1"
anlory.exec_cmd(cmd)

anlory.short_pause()