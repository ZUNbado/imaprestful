from flask import request
from flask.ext.restful import Resource, fields, marshal_with, reqparse
from common.imap import getLogin

class Mail(Resource):
    def get(self, mailbox, uid = None):
        client = getLogin()
        if not client['status']: return client['msg'], 500
        client = client['client']

        parser = reqparse.RequestParser()
        parser.add_argument('markSeen', type=bool, default=False)
        parser.add_argument('markUnseen', type=bool, default=False)
        args = parser.parse_args()

        if uid:
            search = 'UID %s' % uid
        else:
            search = 'ALL'
        mails = []
        for mail in client.walk(mailbox, searchCriterion = search):
            m = { 
                'From' : mail.fromWhom, 
                'Subject' : mail.subject ,
                'Status' : mail.flags,
                'uid' : mail.uid
                }
            if uid:
                m['body'] = str(mail.as_message())
            mails.append(m)
            if args['markSeen'] and not args['markUnseen']:
                mail.seen = True
            elif args['markUnseen'] and not args['markSeen']:
                mail.seen = False
        return mails
    
    def delete(self, mailbox, uid):
        client = getLogin()
        if not client['status']: return client['msg'], 500
        client = client['client']

        parser = reqparse.RequestParser()
        parser.add_argument('expunge', type=bool, default=False)
        args = parser.parse_args()

        mail  = list(client.walk(mailbox, 'UID %s' % uid))
        if len(mail) == 1:
            mail[0].deleted = True
            if args['expunge']:
                client.expunge()
        else:
            return 'Error', 500
