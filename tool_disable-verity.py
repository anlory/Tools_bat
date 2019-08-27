import anlory

# adb root
# adb disable-verify

cmd = "adb root"
anlory.exec_cmd(cmd)

cmd = "adb disable-verify"
anlory.exec_cmd(cmd)


anlory.short_pause()