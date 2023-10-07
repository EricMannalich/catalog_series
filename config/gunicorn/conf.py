import multiprocessing
import os

MY_URL_BASE = "http://" #"https://" para direcciones seguras
MY_URL_DIRECCION = "localhost" #poner la direccion dns del sitio, ejemplo: "mapamicrobiologico.cu"
MY_URL_DIRECCION_ALTERNAS = ",127.0.0.1"#poner las direcciones dns del sitio, ejemplo: "mapamicrobiologico.cu"
MY_URL_PUERTO = ":8080" #":433" para direcciones seguras :80 para inseguras
MY_URL = MY_URL_BASE + MY_URL_DIRECCION + MY_URL_PUERTO
SECURE_SSL_HOST = "https://" + MY_URL_DIRECCION
AGE_LOGIN = "31536000"
PROYECT_NAME = 'core'
os.environ["PROYECT_NAME"] = PROYECT_NAME

#https://docs.gunicorn.org/en/latest/configure.html
name = PROYECT_NAME
bind = MY_URL_PUERTO
backlog = 2048
workers = multiprocessing.cpu_count() * 2 + 1
loglevel = 'info'
errorlog = 'errorlog'
accesslog = 'accesslog'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
wsgi_app = name + ".wsgi"
chdir = PROYECT_NAME
#certfile = '/etc/ssl/certs/selfsigned.crt'
#keyfile = '/etc/ssl/private/selfsigned.key'

#Para generar llaves autofirmadas SSL (HTTPS), poner en la consola de linux y seguir instrucciones:
#openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/selfsigned.key -out /etc/ssl/certs/selfsigned.crt
#openssl dhparam -out /etc/ssl/certs/dhparam.pem 2048

#Seguridad
#https://docs.djangoproject.com/en/4.2/ref/settings/
os.environ["ALLOWED_HOSTS"] = MY_URL_DIRECCION + MY_URL_DIRECCION_ALTERNAS
os.environ["DEBUG"] = "0"
os.environ["CSRF_COOKIE_AGE"] = AGE_LOGIN
os.environ["SECURE_HSTS_SECONDS"] = AGE_LOGIN
os.environ["SECURE_SSL_REDIRECT"] = "0"#="1" para https y ="0" para http
os.environ["SECURE_SSL_HOST"] = SECURE_SSL_HOST
os.environ["CSRF_TRUSTED_ORIGINS"] = SECURE_SSL_HOST
os.environ["CORS_ALLOWED_ORIGINS"] = MY_URL
os.environ["CORS_ORIGIN_WHITELIST"] = MY_URL
os.environ["CORS_ALLOWED_ORIGINS_REGEXE"] = ""

#Django static server
os.environ["IS_STATIC_SERVER"] = "0"