from flask import request
import settings
import imapIO


def getLogin():
    try:
        client = imapIO.connect(settings.HOST, user = request.authorization['username'], password = request.authorization['password'])
        return { 'status' : True, 'client' : client }
    except:
        return { 'status' : False, 'msg' : 'Error connecting host' }
