import subprocess

url = "https://www.youtube.com/watch?v=5eXE36P5EEE"
command = ["yt-dlp", "--get-title", "-s", url]

# 用 subprocess.check_output 运行命令并获取输出
title = subprocess.check_output(command)

# 将输出从 bytes 转为 string，并去除末尾的换行符
title = title.decode('utf-8').strip()

print("Title: ", title)
