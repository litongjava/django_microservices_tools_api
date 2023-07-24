# django_microservices_tools_api
### create project
```
django-admin startproject django_microservices_tools_api
cd django_microservices_tools_api
python manage.py startapp youtube_dl
```

### deploy project to linux
python
```
conda create --name django_microservices_tools_api-python39 python=3.9
conda activate django_microservices_tools_api-python39
```
pip
```
cd /root/code/project/django_microservices_tools_api
pip install -r requirements.txt 
```
startup
```
python manage.py runserver 0.0.0.0:8000
```
or
```shell
gunicorn --bind 0.0.0.0:8000 django_microservices_tools_api.wsgi
```