import os
import schemas.clara_items.schema as clara_items_schema
import schemas.response_options.schema as response_options_schema
import schemas.student_classes.schema as student_classes_schema
import schemas.clara_responses.schema as clara_responses_schema
import schemas.whitelist.schema as whitelist_schema

CLARA_ENV="DEV" # Possible values: DEV, PROD
DEBUG=True
PREFERRED_URL_SCHEME="http"

if "CLARA_ENV" in os.environ:
    # Could be PROD?
    CLARA_ENV = os.environ["CLARA_ENV"]

CLARA_FRONTEND_URL = "http://localhost:4200"
if "CLARA_FRONTEND_URL" in os.environ:
    CLARA_FRONTEND_URL=os.environ["CLARA_FRONTEND_URL"]

# Dataporten CLIENT
DATAPORTEN_CLIENT_ID=os.environ["DATAPORTEN_CLIENT_ID"]
DATAPORTEN_CLIENT_SECRET=os.environ["DATAPORTEN_CLIENT_SECRET"]
# Dataporten ADMIN
DATAPORTEN_ADMIN_CLIENT_ID=os.environ["DATAPORTEN_ADMIN_CLIENT_ID"]
DATAPORTEN_ADMIN_CLIENT_SECRET=os.environ["DATAPORTEN_ADMIN_CLIENT_SECRET"]

# MongoDB
MONGO_DBNAME="clara"
if "MONGO_DBNAME" in os.environ:
    MONGO_DBNAME=os.environ["MONGO_DBNAME"]
MONGO_PORT=27017
if "MONGO_PORT" in os.environ:
    MONGO_PORT=os.environ["MONGO_PORT"]
MONGO_HOST="localhost"
if "MONGO_HOST" in os.environ:
    MONGO_HOST=os.environ["MONGO_HOST"] # sweet-ostrich-mongodb.dev.svc.cluster.local
if "MONGO_USERNAME" in os.environ and "MONGO_PASSWORD" in os.environ:
    MONGO_USERNAME=os.environ["MONGO_USERNAME"] # root
    MONGO_PASSWORD=os.environ["MONGO_PASSWORD"]
    MONGO_AUTH_SOURCE = "admin"

# Redis
REDIS_HOST="localhost"
if "REDIS_HOST" in os.environ:
    REDIS_HOST=os.environ["REDIS_HOST"] # zooming-ladybird-redis-master.dev.svc.cluster.local
REDIS_PASSWORD=None
if "REDIS_PASSWORD" in os.environ:
    REDIS_PASSWORD=os.environ["REDIS_PASSWORD"]

# PROD CONFIGURATION
if CLARA_ENV == "PROD":
    # Disable debug and force https for PROD
    DEBUG=False
    PREFERRED_URL_SCHEME="https"

"""
DO NOT CHANGE ANYTHING BELOW THIS LINE UNLESS YOU KNOW WHAT YOU ARE DOING
"""

URL_PREFIX="v2"
X_DOMAINS="*"
X_HEADERS = ['Authorization','Content-type','Access-Control-Allow-Origin']

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET']

DOMAIN = {
    'clara_items': clara_items_schema.clara_items,
    'response_options': response_options_schema.response_options,
    'student_classes': student_classes_schema.student_classes,
    'clara_responses': clara_responses_schema.clara_responses,
    'whitelist': whitelist_schema.whitelist,
}
