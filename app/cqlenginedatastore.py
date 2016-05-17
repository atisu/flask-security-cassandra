# -*- coding: utf-8 -*-
"""
    cqlenginedatastore
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains an user datastore classes.

    :copyright: (c) 2014 - Attila Marosi <a.cs.marosi@gmail.com>.
"""

from sets import Set
from flask.ext.security import utils
from flask.ext.security.datastore import Datastore, UserDatastore
from flask import current_app

class CQLEngineDatastore(Datastore):
    def put(self, model):
        # TODO: inserting roles does not work (model expects a single UUID).
        dict = {}
        for p in model._values:
            if model._values[p].value is not None:
                dict[p] = model._values[p].value;
        model.create(**dict)
        return model

    def delete(self, model):
        model.delete()


class CQLEngineUserDatastore(CQLEngineDatastore, UserDatastore):
    """A CQLEngine datastore implementation for Flask-Security that assumes
    the use of the Flask-CQLEngine extension.
    """
    def __init__(self, db, user_model, role_model):
        CQLEngineDatastore.__init__(self, db)
        UserDatastore.__init__(self, user_model, role_model)

    def get_user(self, identifier):
        return self.user_model.filter(email=identifier).first()

    def find_user(self, **kwargs):
        q = self.user_model.filter(**kwargs).all()
        try:
            user = q[0]
        except IndexError:
            return None
        # role handling: return a single role for the user
        q = self.role_model.filter(id=user._values['role_id'].value).all();
        try:
            role = q[0]
        except IndexError:
            role = ''
        user.roles = [(role)]
        # add textual representation of role to object. Can be used in
        # templates as current_user.rolename
        user.rolename = role._values['name'].value
        return user

    def find_role(self, role):
        q = self.role_model.filter(name=role).all()
        return q[0]
