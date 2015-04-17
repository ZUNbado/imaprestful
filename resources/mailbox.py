from flask import request
from flask.ext.restful import Resource, fields, marshal_with
from common.imap import getLogin

class Mailbox(Resource):
    def get(self):
        client = getLogin()
        if not client['status']: return client['msg'], 500
        client = client['client']

        folders = []
        for folder in client.folders:
            folders.append(folder[1:-1])
        return folders
