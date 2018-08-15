import os

DEBUG=True
MONGO_HOST="sweet-ostrich-mongodb.dev.svc.cluster.local"
MONGO_PORT=27017
MONGO_DBNAME="eve"
MONGO_USERNAME="root"
MONGO_PASSWORD=os.environ["MONGO_PASSWORD"]
MONGO_AUTH_SOURCE = "admin"
MONGO_REPLICA_SET = "rsname"

DOMAIN = {'people': {}}
