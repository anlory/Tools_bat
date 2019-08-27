import anlory


# adb root
# adb shell settings put global device_provisioned 1
# adb shell settings put secure user_setup_complete 1
# adb shell pm disable com.android.provision


cmdlist = [
"adb root",
"adb shell settings put global device_provisioned 1",
"adb shell settings put secure user_setup_complete 1",
"adb shell pm disable com.android.provision"
]

anlory.exec_cmdlist(cmdlist)

anlory.short_pause()