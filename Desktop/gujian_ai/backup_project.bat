@echo off
cd /d "D:\gujian_ai"
set "BACKUP_NAME=gujian_ai_full_backup_%date:~0,4%%date:~5,2%%date:~8,2%.zip"
tar -a -c -f "%BACKUP_NAME%" *
echo 备份包已生成在 D:\gujian_ai
echo 文件名：%BACKUP_NAME%
pause