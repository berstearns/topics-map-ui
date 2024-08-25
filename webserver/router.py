from flask import Blueprint, render_template,\
                send_from_directory, redirect,\
                request, current_app, url_for,\
                jsonify
import json
from topics import state

main_router = Blueprint('main', __name__)

@main_router.route('/homepage/<keypass>')
def index(keypass):
    print(current_app.sessions)
    print(keypass)
    username_or_none = current_app.sessions.get(keypass)
    if username_or_none is not None:
        user = current_app.database["users"].get(username_or_none)
        state["user"] = user
        response = render_template('./index.html',state=json.dumps(state))
    else:
        response = redirect('/login')
    return response

@main_router.route('/login',methods=["GET"])
def login_view():
    return render_template('./login.html')


@main_router.route('/public/<path:filename>')
def send_js(path):
    return send_from_directory('public', filename)

@main_router.route('/')
@main_router.route('/<first>')
@main_router.route('/<first>/')
@main_router.route('/<first>/<path:rest>')
def fallback(first=None, rest=None):
    return redirect('/login')
