# Installation guide

## Pre Requirements:

- Python 3  (version 3.6.5 was used during the making of this guide)
  Example guide: https://www.rosehosting.com/blog/how-to-install-python-3-6-4-on-centos-7/
- MongoDB   (version 4.0.3 was used during the making of this guide)
  https://docs.mongodb.com/manual/administration/install-on-linux/
- Redis     (version 5.0.0 was used during the making of this guide)     
  https://redis.io/
- Apache with WSGI
  Example guides: https://www.linode.com/docs/web-servers/apache/install-and-configure-apache-on-centos-7/
                  http://flask.pocoo.org/docs/1.0/deploying/mod_wsgi/

## Environment variables (You can skip those who defaults to correct values)

NB! If you don't want to use the `/etc/sysconfig/httpd` file you could choose another way
or directly edit the `settings.py` file in the project folder.

Add these variables in `/etc/sysconfig/httpd`:
- CLARA_ENV=PROD
- CLARA_FRONTEND_URL=https://<FRONTEND_DOMAIN>
- MONGO_DBNAME=<DATABASE_NAME>                  (Default: `clara`)
- MONGO_PORT=<MONGODB_PORT>                     (Default: `27017`)
- MONGO_HOST=<MONGODB_HOST>                     (Default: `localhost`)
- MONGO_USERNAME=<MONGODB_USERNAME>
- MONGO_PASSWORD=<MONGODB_PASSWORD>
- REDIS_HOST=<REDIS_HOST>                       (Default: `localhost`)
- REDIS_PASSWORD=<REDIS_PASSWORD>

## Dataporten setup

This project requires two Applications registered in Dataporten Dashboard,
one for normal users and one for admin access.

### Application 1

- Name: your choice (example: Læringskraft USER)
- Redirect URI: `https://<BACKEND_DOMAIN>/callback?provider=dataporten`
- Accepted scopes: `userid`

On the production server, add these environment variables in `/etc/sysconfig/httpd`:
- DATAPORTEN_CLIENT_ID=<Client ID>
- DATAPORTEN_CLIENT_SECRET=<Client Secret>

### Application 2

- Name: Your choice (example: Læringskraft ADMIN)
- Redirect URI: `https://<BACKEND_DOMAIN>/callback?provider=dataporten_admin`
- Accepted scopes: `email`, `profile`, `userid`, `userid-feide`

On the production server, add these environment variables in `/etc/sysconfig/httpd`:
- DATAPORTEN_ADMIN_CLIENT_ID=<Client ID>
- DATAPORTEN_ADMIN_CLIENT_SECRET=<Client Secret>

NB! Remember to reboot your server after you are finished with the environment file.

## Python Environment Setup

Clone the project somewhere
`cd /var/www/`
`sudo git clone https://github.com/uit-no/clara_backend.git`

Go into the directory and make a virtuel environment
`cd clara_backend/`
`sudo python3.6 -m venv venv`
`. venv/bin/activate`

Install Python requirements
`sudo -H pip3.6 install -r requirements.txt`

Check if it runs
`sudo python3 runserver.py`

## Insert user in whitelist

The Admin interface in the application authenticates trough Dataporten and checks a
whitelist in the database. When working on a blank database, or needing access to the
Admin interface for the first time you need to run the whitelist script to insert a
new user.

`python3 add_admin.py -u abc123@uit.no -n Your Name`

## Populate database with questions

To populate the database for the first time modify the three variables `BASE_PATH`, `TOKEN` and `API`
in the script `insert.sh` and run it:

`./insert.sh`

Tip: Get the token by logging in to the Admin part of the frontend and inspect the local storage.
The token is in the entry named `access_token_admin`.

## WSGI Setup

Copy the apache VirtualHost file to your Apache conf directory (may need editing)
`sudo cp conf/clara_backend.conf /etc/httpd/conf.d/`
`sudo systemctl restart httpd.service`
