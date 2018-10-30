from eve import Eve
from eve.methods.post import post_internal
from eve.methods.get import get_internal, getitem_internal
from eve.methods.put import put_internal
from src.clara_responses import ClaraResponses

from flask import redirect, flash, jsonify, request, stream_with_context
from flask_cors import cross_origin
from src.oauth2 import DataportenSignIn
from src.oauth2admin import DataportenAdminSignIn, requires_auth

from bson.json_util import dumps
from bson import ObjectId

import csv
from datetime import datetime
from io import StringIO
from werkzeug.datastructures import Headers
from werkzeug.wrappers import Response

import settings

clara_responses = ClaraResponses()
app = Eve(auth=DataportenSignIn)
# Callback when someone is accessing one item from clara_responses
app.on_fetched_item_clara_responses += clara_responses.item_calculate_score
app.on_fetched_resource_clara_responses += clara_responses.resource_calculate_score

@app.route('/logout')
@cross_origin()
def logout():
    provider = request.args.get('provider')
    if provider == 'dataporten':
        DataportenSignIn().logout()
        response = jsonify(_status="OK",message="Successfully logged out")
    elif provider == 'dataporten_admin':
        DataportenAdminSignIn().logout()
        response = jsonify(_status="OK",message="Successfully logged out")
    else:
        response = jsonify(_status="ERROR",message="Could not log you out")

    return response

@app.route('/authorize')
def oauth_authorize():
    return DataportenSignIn().authorize()

@app.route('/callback')
def oauth_callback():
    provider = request.args.get('provider')
    if provider == 'dataporten':
        oauth2 = DataportenSignIn()
        user_id, access_token = oauth2.callback()
        if user_id is None:
            response = redirect("{}/callback#access_token=ERROR".format(settings.CALLBACK_URL), code=302)
        else:
            response = redirect("{}/callback#access_token={}".format(settings.CALLBACK_URL, access_token), code=302)
    elif provider == 'dataporten_admin':
        oauth2admin = DataportenAdminSignIn()
        user_id, access_token = oauth2admin.callback()
        if user_id is None:
            response = redirect("{}/admin-callback#access_token=ERROR".format(settings.CALLBACK_URL), code=302)
        else:
            response = redirect("{}/admin-callback#access_token={}".format(settings.CALLBACK_URL,access_token), code=302)

    return response

@app.route('/logout-admin')
@cross_origin()
def logout_admin():
    DataportenAdminSignIn().logout()
    return jsonify(_status="OK",message="Successfully logged out")

@app.route('/authorize-admin')
def oauth_authorize_admin():
    return DataportenAdminSignIn().authorize()

@app.route('/student_classes_admin', methods=['GET','POST'])
@app.route('/student_classes_admin/<_id>', methods=['PUT'])
@cross_origin()
@requires_auth
def student_classes_admin(_id=None):
    if request.method == 'POST':
        return dumps(post_internal('student_classes', request.json)[0])
    elif request.method == 'PUT':
        app.data.driver.db['student_classes'].update(
            {"_id": ObjectId(_id)},
            {"$set": request.json}
        )

    return dumps(get_internal('student_classes')[0])

@app.route('/response_options_admin', methods=['GET','POST'])
@cross_origin()
@requires_auth
def response_options_admin(_id=None):
    if request.method == 'POST':
        return dumps(post_internal('response_options', request.json)[0])

    return dumps(get_internal('response_options')[0])

@app.route('/clara_items_admin', methods=['GET','POST'])
@cross_origin()
@requires_auth
def clara_items_admin(_id=None):
    if request.method == 'POST':
        return dumps(post_internal('clara_items', request.json)[0])

    return dumps(get_internal('clara_items')[0])

@app.route('/whitelist_admin', methods=['GET','POST'])
@app.route('/whitelist_admin/<_id>', methods=['PUT'])
@cross_origin()
@requires_auth
def whitelist_admin(_id=None):
    if request.method == 'POST':
        return dumps(post_internal('whitelist', request.json)[0])
    elif request.method == 'PUT':
        app.data.driver.db['whitelist'].update(
            {"_id": ObjectId(_id)},
            {"$set": request.json}
        )

    return dumps(get_internal('whitelist')[0])

@app.route('/clara_responses_download')
@cross_origin()
@requires_auth
def clara_responses_download():
    items = (get_internal('clara_responses')[0])['_items']
    # print(items)

    def generate():
        data = StringIO()
        w = csv.writer(data, delimiter=';')

        for item in ['main_scale', 'clara_item']:
            header = []
            for res in items[0]['clara_items']:
                header.append(res['clara_item'][item])

            # write header
            w.writerow(header)
            yield data.getvalue()
            data.seek(0)
            data.truncate(0)

        # write each log item
        for item in items:
            # resH = []
            resA = []
            for res in item['clara_items']:
                # resH.append(res['clara_item']['itembank_id'])
                resA.append(res['response_option']['response_value'])

            # w.writerow(resH)
            w.writerow(resA)
            yield data.getvalue()
            data.seek(0)
            data.truncate(0)

    # add a filename
    headers = Headers()
    try:
        headers.set('Content-Disposition', 'attachment', filename='{}.csv'.format(items[0]['student_class']['student_class']))
    except IndexError:
        headers.set('Content-Disposition', 'attachment', filename='empty.csv')
    # stream the response as the data is generated
    return Response(
        stream_with_context(generate()),
        mimetype='text/csv', headers=headers
    )

@app.route('/clara_responses_admin')
@cross_origin()
@requires_auth
def clara_responses_admin():
    return dumps(get_internal('clara_responses')[0])

if __name__ == '__main__':
    app.run(host='0.0.0.0')
