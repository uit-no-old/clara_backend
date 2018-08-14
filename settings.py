import os

MONGO_HOST="sweet-ostrich-mongodb.dev.svc.cluster.local"
MONGO_PORT=27017
MONGO_DBNAME="eve"
MONGO_USERNAME="root"
MONGO_PASSWORD=os.environ.get("MONGO_PASSWORD")

DOMAIN = {'people': {}}
