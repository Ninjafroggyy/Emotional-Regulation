import base64
import hashlib
import requests
import secrets

from flask import Flask, render_template, redirect, request, session, url_for
from flask_cors import CORS
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from okta.models.user import User

app = Flask(__name__)
app.config.update({'SECRET_KEY': secrets.token_hex(64)})
CORS(app)

login = LoginManager()
login.init_app(app)


@login.user_loader
def load_user(user_id):
    return User.get(user_id)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/login")
def login():
    session['app_state'] = secrets.token_urlsafe(64)
    session['code_verifier'] = secrets.token_urlsafe(64)

    hashed = hashlib.sha256(session['code_verifier'].encode('ascii')).digest()
    encoded = base64.urlsafe_b64encode(hashed)
    code_challenge = encoded.decode('ascii').strip('=')

    configuration = {'client_id': config["client_id"],
                    'redirect_uri': config["redirect_uri"],
                    'scope': "openid email profile",
                    'state': session['app_state'],
                    'code_challenge': code_challenge,
                    'code_challenge_method': 'S256',
                    'response_type': 'code',
                    'response_mode': 'query'}

    request_uri = "{base_url}?{configuration}".format(
        base_url=config["auth_uri"],
        configuration=requests.compat.urlencode(configuration)
    )

    return redirect(request_uri)


@app.before_request
def check_valid_login():
    endpoint_group = ('/profile', '/logout')
    if request.endpoint in endpoint_group and not is_authenticated():
        return render_template('login.html', next=request.endpoint)


@app.route("/profile")
@login_required
def profile():
    return render_template("profile.html", user=current_user)


@app.route("/authorization-code/callback")
def callback():
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    code = request.args.get("code")
    app_state = request.args.get("state")
    if app_state != session['app_state']:
        return "App state is incorrect"
    if not code:
        return "The code is not accessible", 403
    configuration2 = {'grant_type': 'authorization_code',
                'code': code,
                'redirect_uri': request.base_url,
                'code_verifier': session['code_verifier']}
    configuration2 = requests.compat.urlencode(configuration2)
    exchange = requests.post(config["token_uri"], headers=headers, data=configuration2, auth=(config["client_id"], config["client_secret"]),).json()

    if not exchange.get("token_type"):
        return "Unsupported token type. Should be 'Bearer'.", 403
    access_token = exchange["access_token"]
    id_token = exchange["id_token"]

    userinfo_response = requests.get(config["userinfo_uri"], headers={'Authorization': f'Bearer {access_token}'}).json()
    unique_id = userinfo_response["sub"]
    user_email = userinfo_response["email"]
    user_name = userinfo_response["given_name"]

    user = User(id_=unique_id, name=user_name, email=user_email)

    if not User.get(unique_id):
        User.create(unique_id, user_name, user_email)

    login_user(user)

    return redirect(url_for("profile"))


@app.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))


config = {
    "auth_uri": "https://dev-85691159.okta.com/oauth2/default/v1/authorize",
    "client_id": "0oa6x1uz853sPOvph5d7",
    "client_secret": "SLKuGvrpikPmduYZYkpHAKzqwmslU5xDk8qVA7A5",
    "redirect_uri": "http://localhost:5000/authorization-code/callback",
    "issuer": "https://dev-85691159.okta.com/oauth2/default",
    "token_uri": "https://dev-85691159.okta.com/oauth2/default/v1/token",
    "userinfo_uri": "https://dev-85691159.okta.com/oauth2/default/userinfo"
}


if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)

