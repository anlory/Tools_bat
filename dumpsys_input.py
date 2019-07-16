import anlory


cmd = "adb shell dumpsys input > " + "debug/dumpsys_input_"+anlory.get_time().strip()+".txt"
# os.system();
print(cmd)
anlory.exec_cmd(cmd);

anlory.short_pause()