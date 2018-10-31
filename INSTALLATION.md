# Installation guide

## Pre Requirements:
- MongoDB   (version 4.0.3 was used during the making of this guide)
  https://docs.mongodb.com/manual/administration/install-on-linux/
- Redis     (version 5.0.0 was used during the making of this guide)     
  https://redis.io/
- Apache with WSGI
  Example guides: https://www.linode.com/docs/web-servers/apache/install-and-configure-apache-on-centos-7/
                  http://flask.pocoo.org/docs/1.0/deploying/mod_wsgi/

## Environment variables (You can skip those who defaults to correct values)
Add these variables in `/etc/environment`:
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

On the production server, add these environment variables in `/etc/environment`:
- DATAPORTEN_CLIENT_ID=<Client ID>
- DATAPORTEN_CLIENT_SECRET=<Client Secret>

### Application 2
- Name: Your choice (example: Læringskraft ADMIN)
- Redirect URI: `https://<BACKEND_DOMAIN>/callback?provider=dataporten_admin`
- Accepted scopes: `email`, `profile`, `userid`, `userid-feide`

On the production server, add these environment variables in `/etc/environment`:
- DATAPORTEN_ADMIN_CLIENT_ID=<Client ID>
- DATAPORTEN_ADMIN_CLIENT_SECRET=<Client Secret>

## API Setup
