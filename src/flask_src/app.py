from flask import Flask
from flask_marshmallow import Marshmallow
from .models import base, db

app = Flask(__name__)
ma = Marshmallow(app)


@app.cli.command('db_create')
def db_create():
    base.metadata.create_all(db)
    print('Database created')


@app.cli.command('db_drop')
def db_drop():
    base.metadata.drop_all(db)
    print('Database dropped')


from .main import *
from .routes.users import *


if __name__ == '__main__':
    app.run(debug=True)
