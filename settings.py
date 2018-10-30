import os
import schemas.clara_items.schema as clara_items_schema
import schemas.response_options.schema as response_options_schema
import schemas.student_classes.schema as student_classes_schema
import schemas.clara_responses.schema as clara_responses_schema
import schemas.whitelist.schema as whitelist_schema

AZURE_ENV = False
try:
    os.environ["MONGO_PASSWORD"]
    AZURE_ENV = True
except KeyError:
    pass

# Test

# Database configuration
if AZURE_ENV:
    DEBUG=True
    MONGO_HOST="sweet-ostrich-mongodb.dev.svc.cluster.local"
    MONGO_PORT=27017
    MONGO_DBNAME="eve"
    MONGO_USERNAME="root"
    MONGO_PASSWORD=os.environ["MONGO_PASSWORD"]
    MONGO_AUTH_SOURCE = "admin"

    CALLBACK_URL = "https://clara-frontend.azurewebsites.net"

    REDIS_HOST="zooming-ladybird-redis-master.dev.svc.cluster.local"
else:
    DEBUG=True
    MONGO_HOST="localhost"
    MONGO_PORT=27017
    MONGO_DBNAME="eve"

    CALLBACK_URL = "http://localhost:4200"
    # CALLBACK_URL = "http://129.242.6.208:4200"

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
