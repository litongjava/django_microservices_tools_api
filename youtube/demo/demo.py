import os.path
import re
import subprocess


def index():
    url = ""
    command = ["yt-dlp", "-f 139", url]
    output = None
    try:
        output = subprocess.check_output(command)
        output = output.decode('utf-8').strip()
    except subprocess.CalledProcessError as e:
        print("The command failed with exit status: ", e.returncode)
        print("output:", e.output.decode('utf-8').strip())
        print("stdout:", e.stdout.decode('utf-8').strip())
        print("stderr:", e.stderr)
        return

    print("the command success and output", output)
    filename = None
    if 'has already been downloaded' in output:
        filename = re.search(r'\[download\] (.+?) has already been downloaded', output).group(1)
        print(filename)
    else:
        match = re.search(r"Destination: (.*)", output)
        if not match:
            return
        filename = match.group(1)

    print("Filename: ", filename)
    if not os.path.exists(filename):
        print("file does not exists")
        return
    print("return file")


index()
