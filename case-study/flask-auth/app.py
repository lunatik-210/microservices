#!flask/bin/python
from app import db, create_app
from flask.ext.script import Manager
from app.commands import CreateStaticData

manager = Manager(create_app)

@manager.command
def create_db():
    db.create_all()

@manager.command
def drop_db():
    db.drop_all()

@manager.command
def recreate_db():
    drop_db()
    create_db()
    CreateStaticData().run()

manager.add_command('create_static_data', CreateStaticData())

manager.add_option('-c', '--config', dest='config', required=False)

if __name__ == '__main__':
    manager.run()
