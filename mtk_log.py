import os, sys
import time

# os.popen()  return
def exec_cmd_return(cmd):
	return os.popen(cmd).read()
# os.system() no return
def exec_cmd(cmd):
	return os.system(cmd)
def get_time():
	return time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
	
def isDeviceExist():
	ret = os.popen("adb devices").readlines()
	return len(ret) == 2

if isDeviceExist():
	print("No devices Found...")
	time.sleep(10)
	sys.exit()
	
print("Log Get Enter...")	
phoneType = exec_cmd_return("adb shell getprop ro.vendor.product.model")
now_time = get_time()
dir = phoneType.strip()+'_'+now_time.strip()+"_log"
os.mkdir(dir)
os.chdir(dir)

exec_cmd("adb pull /sdcard/mtklog")
exec_cmd("adb pull /data/aee_exp  ./system_db")
exec_cmd("adb pull /data/vendor/mtklog/aee_exp  ./vendor_db")
exec_cmd("adb pull /data/anr  ./anr")
exec_cmd("adb pull /data/tombstones  ./tombstones")

print("Get Log Success!")
anlory.short_pause()
