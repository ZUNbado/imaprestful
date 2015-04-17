from flask import request
from flask.ext.restful import Resource, fields, marshal_with
from common.imap import getLogin

class Mail(Resource):
    def get(self, mailbox, uid = None):
        client = getLogin()
        if not client['status']: return client['msg'], 500
        client = client['client']


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
        return mails
