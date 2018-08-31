@echo off
if "%1"=="" (goto :NoFile) else echo 
java -jar tools/chkbugreport-0.5-215.jar %1
ping -n 30 127.0.0.1 > nul
exit


:NoFile
	echo Please input bugreport File...
ping -n 5 127.0.0.1 > nul