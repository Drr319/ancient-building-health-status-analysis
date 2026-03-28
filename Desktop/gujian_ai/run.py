# run.py
import subprocess
import sys

def main():
    # 启动本地服务
    print("🚀 启动项目服务...")
    subprocess.run(["python", "app.py"])

if __name__ == "__main__":
    main()