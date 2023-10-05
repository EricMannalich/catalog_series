import multiprocessing
import os

MY_URL_BASE = "https://"
MY_URL_DIRECCION = "127.0.0.1"
MY_URL_PUERTO = ":443"
MY_URL = MY_URL_BASE + MY_URL_DIRECCION + MY_URL_PUERTO
AGE_LOGIN = "31536000"

#https://docs.gunicorn.org/en/latest/configure.html
name = 'core'
bind = MY_URL_PUERTO
backlog = 2048
workers = multiprocessing.cpu_count() * 2 + 1
loglevel = 'info'
errorlog = 'errorlog'
accesslog = 'accesslog'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
wsgi_app = name + ".wsgi"
chdir = 'core'
certfile = '/etc/ssl/certs/selfsigned.crt'
keyfile = '/etc/ssl/private/selfsigned.key'

#Seguridad
#https://docs.djangoproject.com/en/4.2/ref/settings/
os.environ["SECRET_KEY"]="xuT<llqg<k4xUGHd"
os.environ["ALLOWED_HOSTS"]="*"
os.environ["DEBUG"]="0"
os.environ["CSRF_COOKIE_SECURE"]="1"
os.environ["CSRF_COOKIE_AGE"]=AGE_LOGIN
os.environ["SESSION_COOKIE_SECURE"]="1"
os.environ["SECURE_HSTS_SECONDS"]=AGE_LOGIN
os.environ["SECURE_SSL_REDIRECT"]="1"
os.environ["SECURE_SSL_HOST"]="https://" + MY_URL_DIRECCION + ":443"
os.environ["CORS_ORIGIN_ALLOW_ALL"]="0"
os.environ["CSRF_TRUSTED_ORIGINS"]=MY_URL
os.environ["CORS_ALLOWED_ORIGINS"]=MY_URL
os.environ["CORS_ORIGIN_WHITELIST"]=MY_URL
os.environ["CORS_ALLOWED_ORIGINS_REGEXE"]=""
os.environ["DEFAULT_PERMISSION_ENV"]="rest_framework.permissions.IsAuthenticated"

#BD
os.environ["POSTGRES_USER"]="postgres"
os.environ["POSTGRES_PASSWORD"]="postgres"