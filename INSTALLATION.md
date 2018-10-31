# Installation guide

## Pre Requirements:
- MongoDB
- Redis

## Environment variables
Add these variables in `/etc/environment`:
- CLARA_ENV=PROD
- 


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
