# AnimeCard

## Steps to run in development mode (Windows 10/11):

1. Install `Git` and clone the repository:

You can download `Git`: https://git-scm.com/downloads

```bash
git clone https://github.com/EricMannalich/catalog_series.git
cd catalog_series
```
2. Install `Python 3.11`. Be sure to check the following options:

You can download `Python`: https://www.python.org/downloads

*  Use admin privileges
*  Add python.exe to PATH
*  Customize installation
*  All the "Optional Features"
*  Install Python 3.11 for all user
*  Associate files with Python
*  Create shortcuts for installed applications
*  Add Python to environment variables
*  Precompile standard library
*  Disable path length limit

3. Install and create the virtual environment.

```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
wsl --set-default-version 2
pip install virtualenv 
virtualenv env
```
If Windows does not recognize the `virtualenv` command it is necessary to add the folder where it was installed to the `PATH` of the system environment variables. For this you can press the `Windows + R` keys and execute the following command:

```bash
rundll32.exe sysdm.cpl,EditEnvironmentVariables
```
Now in `User variables` select `Path` and add the path where the package was installed, for example:

```bash
C:\Users\<nombre_usuario>\AppData\Roaming\Python\Python311\Scripts
```

The above path depends on the location where Windows installed the package.

4. Activate the virtual environment and install the Python dependencies from the `requirements.txt` file. Use the commands:

```bash
./env/Scripts/Activate.ps1
pip install -r requirements.txt
```

5. Install `PostgreSQL 15`. Make sure to set the username and password to match the configuration file in `settings.py`, usually `postgres`.

You can download `PostgreSQL`: https://www.enterprisedb.com/downloads/postgres-postgresql-downloads

6. Create a DB in `postgres` with the parameters:

*  POSTGRES_BD = "Media"
*  POSTGRES_USER = "postgres"
*  POSTGRES_PASSWORD = "postgres"
*  POSTGRES_HOST ="127.0.0.1"
*  POSTGRES_PORT ="5432"

7. Open `CMD` where the `manage.py` file is and put the commands:

```bash
python manage.py makemigrations #Prepare DB changes
python manage.py migrate        #Performs DB changes
python manage.py serie --import #Import the DB with the files in the bd_backup folder
python manage.py runserver      #Runs the development server
```
On Windows you can run `run.bat` to run the server. It only works if the virtual environment `env` was previously created and is located in the same folder as `run.bat`.

9. You can create your own user using the command:

```bash
  python manage.py createsuperuser
```
10. They must create an `.env` file with the application credentials:

```bash
# Django
DJANGO_SECRET_KEY = "<your app key goes here>"

# Postgres
POSTGRES_CLIENT_BD = "Media"
POSTGRES_CLIENT_USER = "postgres"
POSTGRES_CLIENT_PASSWORD = "postgres"

# Google
GOOGLE_CLIENT_KEY = "<your app key goes here>"
GOOGLE_CLIENT_SECRET = "your app secret goes here"
```
When you enter the page you can log in with Google and a non-administrative user will be automatically created for you.

## Steps to run in deployment mode (DOCKER):

1. Install `DOCKER`.

You can download `DOCKER`: https://www.docker.com/products/docker-desktop

2. Run `DOCKER`.

3. Install the images of `DOCKER`:

```bash
docker pull python:3.11
docker pull postgres:15
```

In case you already have the images saved locally, replace step 3 with step 4.

4. Load the images from `DOCKER` with the following commands:

```bash
docker load -i media-card-latest.tar
docker load -i postgres-15.3.tar
```
5.  Open `CMD` where the `Dockerfile` file is located and enter the command:

```bash
docker build --force-rm -t media-card:latest .
```

6. Install the latest version of `pgAadmin`.

You can download `pgAadmin`: https://www.pgadmin.org/download/pgadmin-4-windows

7. Send to create the container (standing where the `docker-compose.yml` file is) with the command:

```bash
  docker-compose up
```
8. In the `Docker` application go to `Containers`, inside `core` select `django-animecard`. 

Now you can use the `Files` option to copy the SSL security certificates to the corresponding folders to use the HTTPS secure protocol:
* '/etc/ssl/certs/selfsigned.crt' * '/etc/ssl/certs/selfsigned.crt'
/etc/ssl/private/selfsigned.key'.

In case you do not have these files use the `Terminal` option to generate them with the following commands:

```bash
  openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/selfsigned.key -out /etc/ssl/certs/selfsigned.crt
```
Answer the questions in the previous command and then execute:
```bash
  openssl dhparam -out /etc/ssl/certs/dhparam.pem 2048
```

9. Open the `pgAadmin` and create a new server with the following parameters:

*	Name: (any)
*	Host name: 127.0.0.1
*	Port: 5433
*	Manintenace database: postgres
*	Username: postgres
*	Password: postgres

Then add a database:
* Database: Media

10. Run the `core` container with the interface buttons. Wait until the icon turns green. 

11. You can create your own user using the command (with the `Terminal` option in step 8):

```bash
  python manage.py createsuperuser
```
12. They must create an `.env` file with the application credentials:

```bash
# Django
DJANGO_SECRET_KEY = "<your app key goes here>"

# Google
GOOGLE_CLIENT_KEY = "<your app key goes here>"
GOOGLE_CLIENT_SECRET = "your app secret goes here"
```
When you enter the site you can log in with Google and a non-administrative user will be created automatically.

## Steps to run in online deployment mode (LINUX):

https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-22-04

https://realpython.com/django-nginx-gunicorn/

1. Install `Ubuntu22.04` and the necessary applications. Use the commands:

```bash
sudo apt update
sudo apt upgrade
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install vim curl wget gpg gnupg2 software-properties-common apt-transport-https lsb-release ca-certificates
sudo apt policy postgresql
sudo curl -fsSL https://www.postgresql.org/media/keys/ACCC4CF8.asc|sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/postgresql.gpg
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
sudo apt update
sudo apt upgrade
sudo apt install python3.11 python3-pip python3.11-venv python3.11-dev libpq-dev python3.11-distutils python3.11-tk python3.11-gdbm python3.11-lib2to3 postgresql postgresql-contrib nginx
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.11 1
```

2. Clone the repository, create a virtual environment and install the dependencies. Use the commands:

```bash
git clone https://github.com/EricMannalich/catalog_series.git
cd ~/catalog_series
python -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

sudo touch .env
sudo nano .env
```
3. They must create an `.env` file with the application credentials:

```bash
# Django
DJANGO_SECRET_KEY = "<your app key goes here>"
PROYECT_NAME = "core"
DEBUG = "0"
ALLOWED_HOSTS = ".ejemplo.com"
CSRF_TRUSTED_ORIGINS = "https://ejemplo.com"
SECURE_HSTS_SECONDS = "31536000"
SECURE_SSL_HOST = "https://ejemplo.com"
CORS_ALLOWED_ORIGINS = "http://ejemplo.com"
CORS_ORIGIN_WHITELIST = "http://ejemplo.com"
CORS_ALLOWED_ORIGINS_REGEXE = ""
IS_STATIC_SERVER = "0"

# Postgres
POSTGRES_CLIENT_BD = "media"
POSTGRES_CLIENT_USER = "postgres"
POSTGRES_CLIENT_PASSWORD = "postgres"

# Google
GOOGLE_CLIENT_KEY = "<your app key goes here>"
GOOGLE_CLIENT_SECRET = "your app secret goes here"
```

4. Prepare the `PostgreSQL` database, the data must match the `.env` file from the previous step. Use the commands:

```bash
sudo -u postgres psql
CREATE DATABASE mediacard;
ALTER USER postgres WITH PASSWORD 'postgres';
\q

python manage.py collectstatic --noinput
python manage.py makemigrations #Prepare DB changes
python manage.py migrate        #Performs DB changes
python manage.py serie --import #Import the DB with the files in the bd_backup folder.
deactivate 
```

5. Creating systemd Socket and Service Files for Gunicorn:

```bash
sudo nano /etc/systemd/system/gunicorn.socket
```

6. Inside, 

```bash
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
```

7. Modify the `gunicorn.service` file. Access with the following command:

```bash
sudo nano /etc/systemd/system/gunicorn.service
```

Add the following configuration and save:

```bash
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/catalog_series
ExecStart=/home/ubuntu/catalog_series/env/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          core.wsgi:application

[Install]
WantedBy=multi-user.target
```

Activate the configuration with the following commands:

```bash
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
```

8. Creating and opening a new server block in Nginx’s sites-available directory:

```bash
sudo nano /etc/nginx/sites-available/catalog_series
```

Add the following configuration and save:

```bash
server {
    listen 80;
    listen 443;
    server_name .ejemplo.com;#Public IP of the server

    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        autoindex on;
        tcp_nodelay on;
        keepalive_timeout 65;
        gzip_static on;
        alias /home/ubuntu/catalog_series/static/;
    }

    location /media/ {
        autoindex on;
        tcp_nodelay on;
        keepalive_timeout 65;
        gzip_static on;
        alias /home/ubuntu/catalog_series/media/;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }

}
```

Activate the configuration with the following commands:

```bash
sudo ln -s /etc/nginx/sites-available/catalog_series /etc/nginx/sites-enabled
sudo gpasswd -a www-data ubuntu
#sudo systemctl restart gunicorn
sudo systemctl restart nginx
sudo ufw allow 'Nginx Full'
sudo service nginx restart
```

9. HTTPS:
```bash
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot
sudo certbot --nginx --rsa-key-size 4096 --no-redirect
sudo nano /etc/nginx/sites-available/catalog_series
```
10. Creating and opening a new server block in Nginx’s sites-available directory:

```bash
sudo nano /etc/nginx/sites-available/catalog_series
```

Add the following configuration and save:

```bash
server {
    listen 80;
    server_name .ejemplo.com;


    location / {
        return 301 https://$host$request_uri;
    }
}


server {
    server_name .ejemplo.com;
    listen 443 default ssl; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/ejemplo.com/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/ejemplo.com/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot
    ssl_protocols TLSv1.2 TLSv1.3;
    
    ssl_ecdh_curve secp384r1;
    ssl_session_cache shared:SSL:15m;
    ssl_stapling on;
    ssl_stapling_verify on;
    
    resolver 1.1.1.1 8.8.8.8 8.8.4.4 valid=300s;
    resolver_timeout 5s;
    add_header Strict-Transport-Security "max-age=63072000; includeSubdomains";
    add_header X-Frame-Options DENY;
    add_header X-Content-Type-Options nosniff;
    client_max_body_size 1M;

    location = /favicon.ico { access_log off; log_not_found off; }

    location /static/ {
        autoindex on;
        tcp_nodelay on;
        keepalive_timeout 65;
        gzip_static on;
        alias /home/ubuntu/catalog_series/static/;
    }

    location /media/ {
        autoindex on;
        tcp_nodelay on;
        keepalive_timeout 65;
        gzip_static on;
        alias /home/ubuntu/catalog_series/media/;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
```

Activate the configuration with the following commands:

```bash
sudo systemctl restart nginx
sudo service nginx restart
```