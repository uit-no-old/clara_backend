#!/bin/bash

BASE_PATH="@/var/www/clara_backend"
TOKEN="TOKEN"
API="http://127.0.0.1:5000"

# Clara items
curl -d "$BASE_PATH/schemas/clara_items/no.json" -H "Content-Type: application/json" -H "Authorization: Bearer $TOKEN"  "$API/clara_items_admin"

# Response options
curl -d "$BASE_PATH/schemas/response_options/no.json" -H "Content-Type: application/json;" -H "Authorization: Bearer $TOKEN"  "$API/response_options_admin"
