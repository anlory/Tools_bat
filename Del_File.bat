
REM 删除文件（*.bak)
REM 1. 设置文件属性，可能是只读的

REM set WHAT_SHOULD_BE_DELETED=*.bak  
attrib -a -h -s -r *.bak /s
REM 2. 删除
del *.bak /s