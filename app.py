from flask import Flask, render_template, request, url_for


# Host for sending e-mail.
EMAIL_HOST = 'localhost'

# Port for sending e-mail.
EMAIL_PORT = 1025
# Port website runs on
PORT = 8000
DEBUG = True

# Optional SMTP authentication information for EMAIL_HOST.
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False

app = Flask(__name__)


@app.route('/leaderboard', methods=['GET'])
def leaderboard():
    return render_template('leaderBoard.html')


@app.route('/', methods=['GET','POST'])
def index():
    if request.method == "POST":
        #add to email list
        email = request.form['email']
        print email
    return render_template('index.html')


if __name__ == "__main__":
    app.run(port=PORT, host=EMAIL_HOST, debug=DEBUG)
