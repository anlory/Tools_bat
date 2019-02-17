#coding=utf-8
import xml.dom.minidom
import os
from subprocess import call

#默认为清华源
aops_url = "https://aosp.tuna.tsinghua.edu.cn"


# 1. 修改为源码要保存的路径
rootdir = os.getcwd().replace('\\','/')

# 2.获取manifest 库
manifest_path = rootdir + "/manifest"
print(manifest_path)
if os.path.exists(manifest_path):
	os.chdir(manifest_path)
	cmd = "git pull"
else:
	cmd = "git clone "+ aops_url + "/platform/manifest.git "
os.systemos.system(cmd)

# 3. 使用第二步中 manifest 中 default.xml 
dom = xml.dom.minidom.parse(manifest_path + "/default.xml")
root = dom.documentElement



prefix = " git clone " + aops_url
suffix = ".git"  
 
# 4. 循环下载源码
for node in root.getElementsByTagName("project"):
	# os.chdir(rootdir)
	path =  node.getAttribute("path")
	d = rootdir + "/" + path 
	if os.path.exists(d):
		cmd = "git pull"
	else:
		cmd = prefix + node.getAttribute("name") + suffix + "  "+ d
	print("===== Now get "+ d)
	print(cmd)
	os.system(cmd)