from flask import Flask, render_template, request, url_for
from flask.ext.mail import Mail
from flask.ext.mail import Message
# Host for sending e-mail.
HOST = '0.0.0.0'
# Port for sending e-mail.
EMAIL_PORT = 1025
# Port website runs on
PORT = 8000
DEBUG = True

# Optional SMTP authentication information for EMAIL_HOST.
EMAIL_USE_TLS = False

app = Flask(__name__)
mail = Mail(app)

app.config["MAIL_server"] = 'smtp.gmail.com'
app.config['MAIL_USERNAME'] = 'ratbastard153@gmail.com'
app.config['MAIL_PASSWORD'] = 'w1nt3r1sc0m1ng'

@app.route('/helpful_links', methods=['GET'])
def helpful_links():
    return render_template('helpfulLinks.html')


@app.route('/leaderboard', methods=['GET'])
def leaderboard():
    return render_template('leaderBoard.html')


@app.route('/', methods=['GET','POST'])
def index():
    if request.method == "POST":
        #add to email list
        email = request.form['email']

        #sending the request email to major domo
        #spoofing email
        msg = Message("Reply-To:","subscribe buhacknight-list "+email,sender= "ratbastard153@gmail.com" ,recipients=["angrybird106@gmail.com"])
        mail.send(msg)
        print email
    return render_template('index.html')


if __name__ == "__main__":
    app.run(port=PORT, host=HOST, debug=DEBUG)
