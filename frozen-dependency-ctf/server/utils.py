#functions and stuff

import os
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore
from flask_security.models import fsqla


# set up database script
def db_setup(app_in):
        app_in.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", 'pf9Wkove4IKEAXvy-cQkeDPhv9Cb3Ag-wyJILbq_dFw')
        app_in.config['SECURITY_PASSWORD_SALT'] = os.environ.get("SECURITY_PASSWORD_SALT", '146585145368132386173505678016728509634')
        app_in.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        app_in.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
                "pool_pre_ping": True,
        }

        db_in = SQLAlchemy(app_in)

        fsqla.FsModels.set_db_info(db_in)

        class Role(db_in.Model, fsqla.FsRoleMixin):
                pass

        class User(db_in.Model, fsqla.FsUserMixin):
                pass

        # Setup Flask-Security
        user_datastore = SQLAlchemyUserDatastore(db_in, User, Role)
        security = Security(app_in, user_datastore)

        return db_in, user_datastore, security
