from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from glob import glob
import os

#Create app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = 'xyfnordgo49u59'

#Create database
db = SQLAlchemy(app)

#import models and routes 
from journal_app import routes, models

#Checks for any new files in the new_content directory.
#New files will have a title that becomes the title of the post.
#Content will be contained in the text file. 
new_content = glob('journal_app/new_content/*')


#If there is new content (in the form of files), the program loops
#through and adds each to the database, before deleting that content
#to avoid duplication.
if new_content:
    for content in new_content:
        title = content.split('/')[-1]
        title = title.split('.')[0]
        contents = ""

        #File is read and appended to contents
        with open(content, "r") as f:
            for line in f.readlines():
                print('LINE', line)
                contents += line
        os.remove(content)

        new_post = models.Post(title=title, content=content)
        db.session.add(new_post)
        db.session.commit()
