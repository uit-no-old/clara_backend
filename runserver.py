from eve import Eve
from src.clara_responses import ClaraResponses

from flask import redirect, flash, jsonify
from src.oauth2 import DataportenSignIn

clara_responses = ClaraResponses()
app = Eve(auth=DataportenSignIn)
# Callback when someone is accessing one item from clara_responses
app.on_fetched_item_clara_responses += clara_responses.item_calculate_score
app.on_fetched_resource_clara_responses += clara_responses.resource_calculate_score

@app.route('/logout')
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
        return jsonify(_status="ERR",_error={"code":401,"message":"Authentication failed"})

    return jsonify(access_token=access_token)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
