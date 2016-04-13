from flask import Flask, render_template, request, url_for

import smtplib



# Host for sending e-mail.
SERVER = "localhost"

#host of the site
HOST = 'localhost'
# Port for sending e-mail.
# Port website runs on
PORT = 8000
DEBUG = True

app = Flask(__name__)
#app.config['MAIL_USERNAME'] = 'ratbastard153@gmail.com'
#app.config['MAIL_PASSWORD'] = 'w1nt3r1sc0m1ng'

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

        FROM = email
        print(FROM)
        TO = ["angrybird106@gmail.com"]

        SUBJECT = "this is a test"
        TEXT = "did it work?"

        message = """\
        From: %s
        To: %s
        Subject: %s

        %s
        """ % (FROM, ", ".join(TO),SUBJECT,TEXT)

        server = smtplib.SMTP(SERVER)
        server.sendmail(FROM, TO, message)
        server.quit()


        #sending the request email 
        #spoofing email

        print (email)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(port=PORT, host=HOST, debug=DEBUG)
