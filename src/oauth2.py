import json
import os

from eve.auth import BasicAuth
from rauth import OAuth2Service
from flask import url_for, request, redirect, Response, abort

from redis import StrictRedis

class DataportenSignIn(BasicAuth):
    def __init__(self):
        super(DataportenSignIn, self).__init__()

        self.provider_name = 'dataporten'
        self.consumer_id = os.environ['DATAPORTEN_CLIENT_ID']
        self.consumer_secret = os.environ['DATAPORTEN_CLIENT_SECRET']

        self.service = OAuth2Service(
            name=self.provider_name,
            client_id=self.consumer_id,
            client_secret=self.consumer_secret,
            authorize_url='https://auth.dataporten.no/oauth/authorization',
            access_token_url='https://auth.dataporten.no/oauth/token',
            base_url='https://auth.dataporten.no/'
        )

        self.redis = StrictRedis()

    def authorize(self):
        return redirect(self.service.get_authorize_url(
            client_id=self.consumer_id,
            response_type='code',
            redirect_uri=self.get_callback_url())
        )

    def callback(self):
        def decode_json(payload):
            return json.loads(payload.decode('utf-8'))

        if 'code' not in request.args:
            return None, None, None
        raw_access_token = self.service.get_raw_access_token(
            data={'code': request.args['code'],
                  'grant_type': 'authorization_code',
                  'redirect_uri': self.get_callback_url()}
        )
        response = decode_json(raw_access_token.content)
        oauth_session = self.service.get_session(token=response['access_token'])

        userinfo = oauth_session.get('userinfo').json()
        # Validate that the audience is the same as the client_id
        if (userinfo['audience'] != os.environ['DATAPORTEN_CLIENT_ID']):
            return None, None

        # Store the access_token as key with the user_id as value with an expiration time
        self.redis.set(response['access_token'], userinfo['user']['userid'], response['expires_in'])

        return userinfo['user']['userid'], response['access_token']

    def get_callback_url(self):
        #TODO: This may not be the best check for Azure environment
        try:
            os.environ["MONGO_PASSWORD"]
            return url_for('oauth_callback', provider=self.provider_name, _external=True, _scheme="https")
        except KeyError:
            return url_for('oauth_callback', provider=self.provider_name, _external=True)


    def logout(self):
        """ Delete the stored token
        """
        try:
            token = request.headers.get('Authorization').split(' ')[1]
            self.redis.delete(token)
            return True
        except:
            return False

    def check_auth(self, token, allowed_roles, resource, method):
        """ Check if API request is authorized.
        Examines token in header and checks Redis cache to see if token is
        valid. If so, request is allowed.
        :param token: OAuth 2.0 access token submitted.
        :param allowed_roles: Allowed user roles.
        :param resource: Resource being requested.
        :param method: HTTP method being executed (POST, GET, etc.)
        """
        return token and self.redis.get(token)

    def authorized(self, allowed_roles, resource, method):
        """ Validates the the current request is allowed to pass through.
        :param allowed_roles: allowed roles for the current request, can be a
                              string or a list of roles.
        :param resource: resource being requested.
        """
        try:
            token = request.headers.get('Authorization').split(' ')[1]
        except:
            token = None
        return self.check_auth(token, allowed_roles, resource, method)

    def authenticate(self):
        """ Returns a standard a 401 response that enables basic auth.
        Override if you want to change the response and/or the realm.
        """
        resp = Response(
            None, 401
        )
        abort(401, description="Please log in by accessing the /authorize endpoint", response=resp)
