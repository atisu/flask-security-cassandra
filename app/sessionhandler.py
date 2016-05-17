# -*- coding: utf-8 -*-
"""
    sessionhandler
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains a session handler.

    :copyright: (c) 2014 - Attila Marosi <a.cs.marosi@gmail.com>.
"""
from uuid import uuid4
from datetime import datetime, timedelta

from flask.sessions import SessionInterface, SessionMixin
from werkzeug.datastructures import CallbackDict

from flask import current_app

from models import Session
import json

class CassandraSession(CallbackDict, SessionMixin):

    def __init__(self, initial=None, sid=None):
        CallbackDict.__init__(self, initial)
        self.sid = sid
        self.modified = False


class CassandraSessionInterface(SessionInterface):

    def __init__(self, session_timeout=60):
        self.session_timeout = session_timeout;


    def open_session(self, app, request):
        sid = request.cookies.get(app.session_cookie_name)
        if sid:
            _stored_session = Session.filter(sid=sid)
            if _stored_session:
                stored_session = _stored_session.first()
                if stored_session.expiration > datetime.utcnow():
                    return CassandraSession(initial=json.loads(stored_session.data),
                      sid = stored_session.sid);
        sid = str(uuid4())
        return CassandraSession(sid=sid)


    def save_session(self, app, session, response):
        domain = self.get_cookie_domain(app)
        if not session:
            response.delete_cookie(app.session_cookie_name, domain=domain)
            return
        if self.get_expiration_time(app, session):
            expiration = self.get_expiration_time(app, session)
        else:
            expiration = datetime.utcnow() + timedelta(minutes=self.session_timeout)
        _session = Session.filter(sid=session.sid).ttl(self.session_timeout*60).update(data=json.dumps(session), expiration=expiration)
        response.set_cookie(app.session_cookie_name, value=str(session.sid),
                            expires=expiration,
                            httponly=True, domain=domain)
