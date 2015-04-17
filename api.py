from flask import Flask
from flask.ext.restful import Api
from resources.mailbox import Mailbox
from resources.mail import Mail

app = Flask(__name__)
api = Api(app)

api.add_resource(Mailbox, '/mailbox')
api.add_resource(Mail, '/mailbox/mail/<string:mailbox>', '/mailbox/mail/<string:mailbox>/<string:uid>')

if __name__ == '__main__':
    app.run(debug=True)
