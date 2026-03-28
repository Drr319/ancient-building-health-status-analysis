@echo off
chcp 65001 > nul
echo 正在启动古建筑图片分析程序...
echo.

:: 切换到 BAT 所在目录
cd /d "%~dp0"

:: 重点：这里改成运行 predict.py 进行预测
python "predict.py"

:: 程序结束提示
echo.
echo 分析完成，请查看生成的结果文件。
pause