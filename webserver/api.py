from flask import Blueprint, render_template,\
                send_from_directory, redirect,\
                request, current_app, url_for,\
                jsonify

api = Blueprint('api', __name__)


# can i go to homepage ?
@api.route('/login', methods=["POST"])
def login_attempt():
    # Get form data
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Access the database
    users = current_app.database['users']
    print(users)
    print(username, password)


    # Check if user exists and if the password matches
    user = users.get(username)
    if user and user['password'] == password:
        # Login successful, redirect to homepage
        response = jsonify({"success":True, "keypass":"ajiosf12j3oi1ih41o"})
    else:
        # Login failed, re-render the login page with an error message
        flash("Invalid username or password", "error")
        response = jsonify({"success":False, "message":"unexpected error"})
    return response

@api.route('/submit_task',methods=["POST"])
def submit_task():
    # Get form data
    data = request.get_json()

    # Extract the topicId, taskId, and text from the JSON data
    topic_id = data.get('topicId')
    task_id = data.get('taskId')
    text = data.get('text')

    print(data)
    # Check if user exists and if the password matches
    # user = users.get(username)
    return {}
