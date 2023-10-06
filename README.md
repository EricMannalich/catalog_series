# AnimeCard

## Pasos para ejecutar en modo desarrollo (Windows 10/11):

1. Instalar `Git` y clonar el repositorio:

Puede descargar `Git`: https://git-scm.com/downloads

```bash
git clone https://github.com/EricMannalich/catalog_series.git
cd catalog_series
```
2. Instalar `Python 3.11`. Asegúrese de marcar las siguientes opciones:

Puede descargar `Python`: https://www.python.org/downloads

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

3. Instalar y crear el entorno virtual.

```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
wsl --set-default-version 2
pip install virtualenv 
virtualenv env
```
Si Windows no reconoce el comando `virtualenv` es necesario añadir la carpeta donde se instaló al `PATH` de las variables de entorno del sistema. Para esto puede presionar las teclas `Windows + R` y ejecutar el siguiente comando:

```bash
rundll32.exe sysdm.cpl,EditEnvironmentVariables
```
Ahora en `User variables` seleccionar `Path` y agregar la ruta donde se instaló el paquete, por ejemplo:

```bash
C:\Users\<nombre_usuario>\AppData\Roaming\Python\Python311\Scripts
```

La ruta anterior depende de la ubicación donde Windows instaló el paquete.

4. Activar el entorno virtual e instalar las dependencias de Python del archivo `requirements.txt`. Utilizar los comandos:

```bash
./env/Scripts/Activate.ps1
pip install -r requirements.txt
```

5. Instalar `PostgreSQL 15`. Asegúrese de poner el usuario y contraseña que coincida con el archivo de configuracion en `settings.py`, generalmente es: `postgres`.

Puede descargar `PostgreSQL`: https://www.enterprisedb.com/downloads/postgres-postgresql-downloads

6. Crear una BD en postgres con los parámetros:

*  POSTGRES_BD = "Media"
*  POSTGRES_USER = "postgres"
*  POSTGRES_PASSWORD = "postgres"
*  POSTGRES_HOST ="127.0.0.1"
*  POSTGRES_PORT ="5432"

7. Abren `CMD` en donde está el archivo `manage.py` y poner los comandos:

```bash
python manage.py makemigrations #Prepara los cambios de la BD
python manage.py migrate        #Efectua los cambios de la BD
python manage.py serie --import #Importa la BD con los archibos de la carpeta bd_backup
python manage.py runserver      #Ejecuta el servidor de desarrollo
```
En Windows pueden ejecutar `run.bat` para ejecutar el servidor. Solo funciona si fue creado previamente el entorno virtual `env` y se encuentra en la misma carpeta que `run.bat`.

9. Pueden crearse su propio usuario utilizando el comando:

```bash
  python manage.py createsuperuser
```
Al entrar en la página pueden loguearse con Google y se les creara automáticamente un usuario no administrativo.

## Pasos para ejecutar en modo despliegue (DOCKER):

1. Instalar `DOCKER`.

Puede descargar `DOCKER`: https://www.docker.com/products/docker-desktop

2. Ejecutar `DOCKER`.

3. Instalar las imágenes de `DOCKER`:

```bash
docker pull python:3.11
docker pull postgres:15
```

En caso de que ya tengan las imágenes guardadas localmente sustituyan el paso 3, por el 4.

4. Cargar las imágenes de `DOCKER` con los siguientes comandos:

```bash
docker load -i media-card-latest.tar
docker load -i postgres-15.3.tar
```
5.  Abren `CMD` en donde está el archivo `Dockerfile` y ponen el comando: 

```bash
docker build --force-rm -t media-card:latest .
```

6. Instalar la última versión de `pgAadmin`.

Puede descargar `pgAadmin`: https://www.pgadmin.org/download/pgadmin-4-windows

7. Mandar a crear el contenedor (parado donde está el archivo `docker-compose.yml`) con el comando:

```bash
  docker-compose up
```
8. En la aplicación de `Docker` entrar a `Containers`, dentro de `core` seleccionar `django-animecard`. 

Ahora puedes utilizar la opción `Files` para copiar los certificados de seguridad SSL en las carpetas correspondientes para utilizar el protocolo seguro HTTPS:
*  '/etc/ssl/certs/selfsigned.crt'
*  '/etc/ssl/private/selfsigned.key'

En caso de no contar con estos archivos utilizar la opción `Terminal` para generarlos con los siguientes comandos:
```bash
  openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/selfsigned.key -out /etc/ssl/certs/selfsigned.crt
```
Responder las preguntas del comando anterior y después ejecutar:
```bash
  openssl dhparam -out /etc/ssl/certs/dhparam.pem 2048
```

9. Abrir el `pgAadmin` y crea un nuevo server con los siguientes parámetros:

*	Name: (cualquiera)
*	Host name: 127.0.0.1
*	Port: 5433
*	Manintenace database: postgres
*	Username: postgres
*	Password: postgres

10. Ejecuta el contenedor `core` con los botones de la interfaz. Espera a que el icono se ponga de color verde.

11. Pueden crearse su propio usuario utilizando el comando (con la opción `Terminal` del paso 8):

```bash
  python manage.py createsuperuser
```
Al entrar en la página pueden loguearse con Google y se les creara automáticamente un usuario no administrativo.

## Pasos para ejecutar en modo despliegue online (LINUX):

1. Instalar `Ubuntu20.04`. Utilizar los comandos:
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

2.	Puedes copiar los sertificados de seguridad SSL en las carpetas correspondientes para utilizar el protocolo seguro HTTPS:
*  '/etc/ssl/certs/selfsigned.crt'
*  '/etc/ssl/private/selfsigned.key'

En caso de no contar con estos archivos se deben generar con los siguientes comandos:
```bash
  sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/selfsigned.key -out /etc/ssl/certs/selfsigned.crt
```
Responder las preguntas del comando anterior y después ejecutar:
```bash
  sudo openssl dhparam -out /etc/ssl/certs/dhparam.pem 2048
```

3. Deberá programar la ejecución automática del servidor:

```bash
  sudo crontab -e
```
Abrirá un archivo de texto, al final deberá agregar los siguientes comandos sustituyendo `usuario` por el nombre de usuario del sistema operativo:
```bash
  SHELL=/bin/bash
  @reboot sh /home/<usuario>/core/run.sh
```
Salve los cambios y reinicie el sistema:
```bash
  sudo reboot
```
4. Pueden crearse su propio usuario utilizando el comando:

```bash
  python manage.py createsuperuser
```
Al entrar en la página pueden loguearse con Google y se les creara automáticamente un usuario no administrativo.