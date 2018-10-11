from eve import Eve
from eve.methods.post import post_internal
from eve.methods.get import get_internal
from src.clara_responses import ClaraResponses

from flask import redirect, flash, jsonify, request
from flask_cors import cross_origin
from src.oauth2 import DataportenSignIn
from src.basic import requires_auth

from bson.json_util import dumps
from bson import ObjectId

clara_responses = ClaraResponses()
app = Eve(auth=DataportenSignIn)
# Callback when someone is accessing one item from clara_responses
app.on_fetched_item_clara_responses += clara_responses.item_calculate_score
app.on_fetched_resource_clara_responses += clara_responses.resource_calculate_score

@app.route('/logout')
@cross_origin()
def logout():
    DataportenSignIn().logout()
    return jsonify(_status="OK",message="Successfully logged out")

@app.route('/authorize')
def oauth_authorize():
    return DataportenSignIn().authorize()

@app.route('/callback')
def oauth_callback():
    oauth2 = DataportenSignIn()
    user_id, access_token = oauth2.callback()
    if user_id is None:
        response = redirect("http://localhost:4200/callback#access_token=ERROR", code=302)
    else:
        response = redirect("http://localhost:4200/callback#access_token={}".format(access_token), code=302)

    return response

@app.route('/student_classes_admin', methods=['GET','POST'])
@requires_auth
def student_classes_admin():
    if request.method == 'POST':
        return dumps(post_internal('student_classes', request.json))
    else:
        return dumps(get_internal('student_classes'))

@app.route('/clara_responses_admin')
@requires_auth
def clara_responses_admin():
    return dumps(get_internal('clara_responses'))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
