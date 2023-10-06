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
*  Todas las "Optional Features"
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

*	Name: (cualquiera)
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

## Pasos para ejecutar en modo despliegue online (LINUX):

1. Install `Ubuntu20.04`. Use the commands:
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
sudo apt install python3.11 python3-pip python3-venv python3-dev libpq-dev postgresql postgresql-contrib

sudo git clone https://github.com/EricMannalich/catalog_series.git
cd ~/catalog_series
sudo -H pip3 install --upgrade pip
sudo python3 -m venv env
source env/bin/activate
sudo pip3 install -r requirements.txt

sudo -u postgres psql
CREATE DATABASE Media;
ALTER USER postgres WITH PASSWORD 'postgres';
\

sudo python3 manage.py makemigrations #Prepara los cambios de la BD
sudo python3 manage.py migrate        #Efectua los cambios de la BD
sudo python3 manage.py serie --import #Importa la BD con los archibos de la carpeta bd_backup

```

2.	You can copy the SSL security certificates to the corresponding folders to use the HTTPS secure protocol:
* '/etc/ssl/certs/selfsigned.crt' * '/etc/ssl/certs/selfsigned.crt'
/etc/ssl/private/selfsigned.crt' * '/etc/ssl/private/selfsigned.key'.

If these files are not available, they must be generated with the following commands:

```bash
  sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/selfsigned.key -out /etc/ssl/certs/selfsigned.crt
```
Answer the questions in the previous command and then execute:
```bash
  sudo openssl dhparam -out /etc/ssl/certs/dhparam.pem 2048
```

3. You will have to program the automatic execution of the server:

```bash
  sudo crontab -e
```
It will open a text file, at the end you should add the following commands replacing `user` with the operating system user name:

```bash
  SHELL=/bin/bash
  @reboot sh /home/<usuario>/core/run.sh
```
Save the changes and reboot the system:
```bash
  sudo reboot
```
4. You can create your own user using the command:

```bash
  python manage.py createsuperuser
```
15. They must create an `.env` file with the application credentials:

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
When you enter the site you can log in with Google and a non-administrative user will be created automatically.