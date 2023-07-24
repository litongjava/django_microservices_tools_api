from django.http import JsonResponse, FileResponse
from django.views.decorators.http import require_http_methods
import os.path
import re
import subprocess


@require_http_methods(["POST"])  # only allow post requests
def download(request):
    # 1. 从 POST 请求中获取下载的 url 和 format
    url = request.POST.get('url')
    format = request.POST.get('format')

    command = ["yt-dlp", f"-f {format}", url]
    output = None
    try:
        output = subprocess.check_output(command)
        output = output.decode('utf-8').strip()
    except subprocess.CalledProcessError as e:
        print("The command failed with exit status: ", e.returncode)
        print("output:", e.output.decode('utf-8').strip())
        print("stdout:", e.stdout.decode('utf-8').strip())
        print("stderr:", e.stderr)
        return JsonResponse({'msg': 'The command failed'}, status=500)

    print("the command success and output", output)
    filename = None
    if 'has already been downloaded' in output:
        filename = re.search(r'\[download\] (.+?) has already been downloaded', output).group(1)
    else:
        match = re.search(r"Destination: (.*)", output)
        if not match:
            return JsonResponse({'msg': 'Destination not found in command output'}, status=500)
        filename = match.group(1)

    print("Filename: ", filename)
    if not os.path.exists(filename):
        print("file does not exists")
        return JsonResponse({'msg': 'File not found on server'}, status=500)

    # 2. 将下载后的文件以下载的方式返回到浏览器
    response = FileResponse(open(filename, 'rb'))
    response['Content-Disposition'] = f'attachment; filename="{os.path.basename(filename)}"'
    print("return file")
    return response
