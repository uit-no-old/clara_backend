import os
import schemas.clara_items.schema as clara_items_schema
import schemas.response_options.schema as response_options_schema

azure = False
try:
    os.environ["MONGO_PASSWORD"]
    azure = True
except KeyError:
    pass

# Database configuration
if azure:
    DEBUG=True
    MONGO_HOST="sweet-ostrich-mongodb.dev.svc.cluster.local"
    MONGO_PORT=27017
    MONGO_DBNAME="eve"
    MONGO_USERNAME="root"
    MONGO_PASSWORD=os.environ["MONGO_PASSWORD"]
    MONGO_AUTH_SOURCE = "admin"
    MONGO_REPLICA_SET = "rsname"
else:
    DEBUG=True
    MONGO_HOST="localhost"
    MONGO_PORT=27017
    MONGO_DBNAME="eve"

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET']

DOMAIN = {
    'clara_items': clara_items_schema.clara_items,
    'response_options': response_options_schema.response_options
}
