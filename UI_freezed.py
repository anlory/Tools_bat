import os, sys
import time


# os.popen()  return
def exec_cmd_return(cmd):
	return os.popen(cmd).read()
# os.system() no return
def exec_cmd(cmd):
	return os.system(cmd)


def getevent():
	filename = "./getevent.txt"
	getevent_file = open(filename, 'w')
	logcmd = "adb shell getevent -l"
	Poplog = subprocess.Popen(logcmd,stdout=getevent_file,stderr=subprocess.PIPE)
	time.sleep(30)
	Poplog.terminate()
print("Get UI Freezed LOG...")


print("-------------------------------------------------")
print("-------------------------------------------------")
print("please preese Power Key Or Volume key manay times")
print("-------------------------------------------------")
getevent()
print("-----------------getevent  success---------------")
cmd = "adb shell ps -A | grep system_server"
ps_result = exec_cmd_return(cmd).split()
pid = ps_result[1]
cmd = "adb shell su 1000 kill -3 "+pid
i = 1
while i <= 3:
	i += 1
	time.sleep(5)
	exec_cmd(cmd)

cmd = "adb shell su 1000 cp /data/anr /sdcard/ -R"
exec_cmd(cmd)
cmd = "adb pull /sdcard/anr  ./anr"
exec_cmd(cmd)

cmd = "adb shell setprop service.bootanim.exit 0 "
exec_cmd(cmd)
cmd = "adb shell setprop ctl.start bootanim "
exec_cmd(cmd)
print("-------------------------------------------------")
print("-------------------------------------------------")
print("please see whether  bootanim start!!			    ")
print("-------------------------------------------------")
time.sleep(10)
cmd = "adb shell setprop service.bootanim.exit 1 "
exec_cmd(cmd)