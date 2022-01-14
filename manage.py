from multiprocessing import managers
from app import create_app, db
from flask_script import Manager, Server
from app.models import User


@managers.shell
def make_shell_context():
    return dict(app=app, db=db, User= User)



if __name__ == '__main__':
    manager.run()