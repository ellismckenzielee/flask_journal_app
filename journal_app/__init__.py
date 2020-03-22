from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from glob import glob
import os

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
        print('CONTENT', content)
        contents = ":"
        with open(content, "r") as f:
            for line in f.readlines():
                print('LINE', line)
                contents += line
        os.remove(content)
        print(contents)

        new_post = models.Post(title=title, content=content)
        db.session.add(new_post)
        db.session.commit()
