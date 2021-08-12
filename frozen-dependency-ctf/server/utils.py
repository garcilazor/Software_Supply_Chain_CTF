#functions and stuff

import os
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore
from flask_security.models import fsqla
from sqlalchemy import Boolean, DateTime, Column, Integer, \
                       String, ForeignKey

# simple user db (singleton)
class SimpleDB():
    __instance = False
    db = None
    user_datastore = None
    security = None

    def __init__(self, db, user_datastore, security):
        if SimpleDB.__instance is False:
            SimpleDB.db = db
            SimpleDB.user_datastore = user_datastore
            SimpleDB.security = security
            SimpleDB.__instance = True

    @staticmethod
    def get():
        if SimpleDB.__instance is False:
            SimpleDB()
        return SimpleDB.db, SimpleDB.user_datastore, SimpleDB.security




# set up database script
def db_setup(app_in):

    app_in.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", 'pf9Wkove4IKEAXvy-cQkeDPhv9Cb3Ag-wyJILbq_dFw')
    app_in.config['SECURITY_PASSWORD_SALT'] = os.environ.get("SECURITY_PASSWORD_SALT", '146585145368132386173505678016728509634')
    app_in.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
    app_in.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
        "pool_pre_ping": True,
    }

    db = SQLAlchemy(app_in)

    fsqla.FsModels.set_db_info(db)

    class Role(db.Model, fsqla.FsRoleMixin):
        pass

    class User(db.Model, fsqla.FsUserMixin):
        profile = db.Column(db.String, nullable=True)
        secret = db.Column(db.String, nullable=True)
        
        def get_data(self):
            return self.profile, self.secret

    # Setup Flask-Security
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security = Security(app_in, user_datastore)

    #store db as singleton
    SimpleDB(db, user_datastore, security)

    return db, user_datastore, security
