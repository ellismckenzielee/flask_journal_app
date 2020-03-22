from journal_app import app, db
from journal_app.models import Post
from flask import render_template

@app.route('/')
def home():
    posts = Post.query.all()
    print(Post)
    return render_template('index.html', posts=posts)

