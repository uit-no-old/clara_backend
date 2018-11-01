#!/usr/bin/python3

import sys, getopt
import settings
from pymongo import MongoClient

def main(argv):
    username = ''
    name = ''
    try:
        opts, args = getopt.getopt(argv,"hu:n:",["username=","name="])
    except getopt.GetoptError:
        print ('add_admin.py -u <username> -n <name>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('add_admin.py -u <username> -n <name>')
            sys.exit()
        elif opt in ("-u", "--username"):
            username = arg
        elif opt in ("-n", "--name"):
            name = arg

    if len(username) == 0 or len(name) == 0:
        print ('add_admin.py -u <username> -n <name>')
        sys.exit(2)        

    try:
        client = MongoClient('mongodb://%s:%s@%s:%s' % (settings.MONGO_USERNAME, settings.MONGO_PASSWORD, settings.MONGO_HOST, settings.MONGO_PORT))
    except AttributeError:
        client = MongoClient('mongodb://%s:%s' % (settings.MONGO_HOST, settings.MONGO_PORT))
    db = client[settings.MONGO_DBNAME]

    whitelist = db.whitelist
    user = {
        "username": username,
        "name": name,
        "active": True
    }

    whitelist_id = whitelist.insert_one(user).inserted_id

    if whitelist_id:
        print('SUCCESS')
    else:
        print('ERROR')

if __name__ == "__main__":
   main(sys.argv[1:])
