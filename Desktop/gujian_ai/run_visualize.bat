@echo off
cd /d "%~dp0"
echo ======================================
echo    古建筑标注数据可视化工具
echo ======================================
echo.
echo 正在生成数据分布图表...
echo.
python visualize_labels.py
echo.
echo ======================================
echo  ✅ 图表已生成：labels_visualization.png
echo  📍 保存在当前 gujian_ai 文件夹中
echo ======================================
echo.
echo 按任意键退出...
pause >nul