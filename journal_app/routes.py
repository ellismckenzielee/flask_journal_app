from journal_app import app, db
from journal_app.models import Post
from journal_app.forms import PostForm
from flask import render_template, redirect, request, url_for


@app.route('/')
def home():
    posts = Post.query.all()
    print(Post)
    return render_template('index.html', posts=posts)

@app.route('/<id>',methods=['GET','POST'])
def detail(id):
    post = Post.query.get(id)
    print('hi')
    return render_template('detail.html', post=post)


@app.route('/<id>/edit',methods=['GET', 'POST'])
def edit(id):
    if request.method=="POST":
        form = request.form
        print(form)
        post = Post.query.get(id)
        post.content = form['content']
        print(post.title, post.content)
        db.session.commit()
        return redirect(url_for('detail', id=post.id))

    form = PostForm()
    post = Post.query.get(id)
    if form.validate_on_submit():
        print('validated_form')
    return render_template('edit.html', form=form, post=post)

@app.route('/<id>/delete',methods=['GET', 'DELETE'])
def delete(id):
    post = Post.query.get(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_form('home'))