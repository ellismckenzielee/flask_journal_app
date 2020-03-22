from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from glob import glob

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

from journal_app import routes, models

new_content = glob('journal_app/new_content/*')

print('NEEWWWW CONTENT ', new_content)
if new_content:
    for content in new_content:
        title = content.split('/')[-1]
        title = title.split('.')[0]
        print(title)

