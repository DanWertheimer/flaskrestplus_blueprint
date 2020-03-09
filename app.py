from flask import Blueprint, g, redirect, request, session, url_for, jsonify, make_response
from flask_cors import CORS
from flask_restplus import Api
from flask_httpauth import HTTPBasicAuth

from main import create_app, ldap
auth = HTTPBasicAuth()

blueprint = Blueprint('api', __name__)


api = Api(blueprint,
          title='<API TITLE>',
          version='0.1',
          description='<API DESCRIPTION>')

# This refers to the namespace created and where it will
# be accessible.
# i.e. localhost:8000/path/
# The NAMESPACE variable should be defined in your API controller
api.add_namespace(NAMESPACE, path='<NS_PATH>')

# create the flask app
app = create_app()
# register blueprint
app.register_blueprint(blueprint)
# assign a key, this should be set randomly for production builds
app.secret_key = 'dev key'
# Apply cross origin resource sharing
CORS(app)


@app.before_request
def before_request():
    """
    Checks if there's an LDAP user logged into the session
    before making a request to the application
    """
    g.user = None
    if 'user_id' in session:
        # This is where you'd query your database to get the user info.
        g.user = {}
        # Create a global with the LDAP groups the user is a member of.
        g.ldap_groups = ldap.get_user_groups(user=session['user_id'])


@auth.verify_password
def verify_password(username, password):
    """create the password verification for ldap users
    """
    # this will return the user information from your
    # LDAP server
    user = ldap.bind_user(username, password)
    if user is None or password == '':
        # If user is None then sign in was unsuccessful
        return False
    else:
        session['user_id'] = username
        return True

# Creates the login page users will have to authenticate against
@app.route('/login', methods=['GET'])
@auth.login_required
def login():
    if g.user:
        return redirect(url_for('index'))
    if request.method == 'GET':
        data = {'user': session['user_id'], 'code': 'SUCCESS'}
        return make_response(jsonify(data), 200)
