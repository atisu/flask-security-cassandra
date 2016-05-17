from flask import Flask, redirect
from flask.ext.cqlengine import CQLEngine

from models import init_db, Users, Role
from sessionhandler import CassandraSessionInterface
from cqlenginedatastore import CQLEngineDatastore, CQLEngineUserDatastore
from flask.ext.security import Security

app = Flask(__name__)
app.session_interface = CassandraSessionInterface(session_timeout = 60)


def init_application(app, config):
    app.config.from_object(config)
    cqlengine = CQLEngine(app)
    init_db()
    user_datastore = CQLEngineUserDatastore(cqlengine, Users, Role)
    security = Security(app, user_datastore)
    app.logger.debug("Flask Application initialized")
