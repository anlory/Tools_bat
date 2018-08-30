@echo off

@adb devices | findstr "\<device\>"
if errorlevel 1 goto NOCONNECTED

:CONNECTED

for /f "skip=1" %%a in ('adb devices') do (
	@echo ======================================
	@echo Start Copy  %%a log
	call :PullLOG %%a 
	@echo End Copy  %%a log
	@echo ======================================
)
@echo  Copy all devices log End
pause
exit




:PullLOG
set device_SN=%1
REM @echo device_SN:%device_SN%
for /f "delims=" %%i in ('adb -s %device_SN% shell  getprop ro.vendor.product.model') do (set model=%%i)

set filename=%model%_%date:~5,2%_%date:~8,2%-%time:~0,2%-%time:~3,2%-%time:~6,2%_%device_SN%

md %filename%



adb -s %device_SN% pull /sdcard/mtklog ./%filename%/mtklog
@echo --------------pull mtklog 	--------------

adb -s %device_SN% pull /data/aee_exp  ./%filename%/system_db
@echo --------------pull aee_exp 	--------------

adb -s %device_SN% pull /data/vendor/mtklog/aee_exp  ./%filename%/vendor_db
@echo --------------pull vendor_db 	--------------

@adb -s %device_SN% pull /data/anr  ./%filename%/anr
@echo --------------pull anr 		--------------


adb -s %device_SN% pull /data/tombstones  ./%filename%/tombstones
@echo --------------pull tombstones --------------

goto:eof




:NOCONNECTED
	@echo ======================================
	@echo Waiting Android Device Connected...
	@echo ======================================
	adb wait-for-device
	goto CONNECTED
	