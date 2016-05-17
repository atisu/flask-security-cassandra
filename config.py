import os
import sys
_basedir = os.path.abspath(os.path.dirname(__file__))
from cassandra.auth import PlainTextAuthProvider

class BaseConfiguration(object):
    DEBUG = False
    TESTING = False
    CQLENGINE_HOSTS = ""
    CQLENGINE_PORT = 9042
    CQLENGINE_DEFAULT_KEYSPACE = ""
    CQLENGINE_USER = ""
    CQLENGINE_PASSWORD = ""
    CQLENGINE_SETUP_KWARGS = { "auth_provider": PlainTextAuthProvider(username=CQLENGINE_USER, password=CQLENGINE_PASSWORD)}
    SECRET_KEY = "";

class DebugConfiguration(BaseConfiguration):
    DEBUG = True
    CQLENGINE_HOSTS = ['host1']
    CQLENGINE_PORT = 9042
    CQLENGINE_DEFAULT_KEYSPACE = "app"
    CQLENGINE_USER = "app"
    CQLENGINE_PASSWORD = "Dm7VvnersYTPtZ87eWmu"
    CQLENGINE_SETUP_KWARGS = {"auth_provider": PlainTextAuthProvider(username=CQLENGINE_USER, password=CQLENGINE_PASSWORD)}
    SECURITY_PASSWORD_HASH = "pbkdf2_sha512"
    SECURITY_PASSWORD_SALT = "Em.o-#$@!&hIYKWP$LqH>D-b6^"
    SECRET_KEY = "bbbbbnnnn";

class TestConfiguration(BaseConfiguration):
    TESTING = True
