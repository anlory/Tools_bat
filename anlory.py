import os, sys
import time



def exec_cmd_return(cmd):
	return os.popen(cmd).read()
    
# os.system() no return
def exec_cmd(cmd):
    print(cmd)
    return os.system(cmd)

def exec_cmdlist(list):
    for cmd in list :
        exec_cmd(cmd)


def get_time():
	return time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
 
def short_pause():
    time.sleep(3)