import os
from flask import render_template,request,redirect,url_for,jsonify
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename

from . import main
from .. import db,photos
from .forms import BookForm
from ..models import User, Books, Chat
from .. import create_app
import app
import pusher

# Views

# THIS IS THE LANDING PAGE BEFORE LOGIN
@main.route('/')
def index():
	title = 'Book Club'
	return render_template('index.html',title = title)


# @main.route('/archives')
# def archives():

# 	return render_template('archives.html')

# @main.route('/specificbook')
# def specific():
# 	return render_template('specificbook.html')







# DISPLAY ALL BOOKS IN THE DB
@main.route('/all_books')
@login_required
def all_books_view():
	all_books = Books.get_books()
	return render_template('archives.html',all_books = all_books)


# UPLOADING NEW BOOK TO THE SYSYTEM
@main.route('/bookupload', methods = ['GET', 'POST'])
@login_required 
def new_book_upload():
	title = 'Book Club'

	form = BookForm()
	if 'photo' in request.files:
		filename = photos.save(request.files['photo'])
		path = f'photos/{filename}'
		title = request.form['title']
		author = request.form['author']
		description = request.form['description']

		new_book = Books(title = title , author = author, description = description, user = current_user,photo = path)
		# new_book = Books(title = title , author = author, description = description,photo = path)
		new_book.save_book()
		return redirect(url_for('.all_books_view'))

	return render_template('bookupload.html', title = title, book_form = form)


# VIEW FULL DETAIbook.photoL ABOUT A CERTAIN BOOK & ITS COMMENTS
@main.route('/book/<int:id>',methods = ['GET','POST'])
@login_required
def single_bk(id):
	chat = Chat.query.all()
	s_book = Books.get_single_book(id)
	posted = s_book.posted.strftime('%b %d, %Y')

	return render_template('specificbook.html', s_book = s_book,date = posted)



# GETTING BOOKS THAT WERE UPLOADED BY THE CURRENT_USER
@main.route('/user/<uname>/books')
def user_books(uname):
    user = User.query.filter_by(username=uname).first()
    books = Books.query.filter_by(user_id = user.id).all()

    return render_template("profile/profile.html", user = user,books = books)


pusher_client = pusher.Pusher(
  app_id='911993',
  key='516cc952f7e807a6d0b3',
  secret='80b9ddcd00bea0ca2037',
  cluster='ap2',
  ssl=True
)

@main.route('/message', methods =['GET','POST'])
def message():
	username = request.form.get('username')
	message = request.form.get('message')

	new_chat =  Chat(username = username , message = message)
	db.session.add(new_chat)
	db.session.commit()

	pusher_client.trigger('chat-channel', 'new-message', {'username': username, 'message': message})

	return render_template('chat.html')

# @main.route('/registercheck')
# def bookupload():
# 	return render_template('auth/register2.html')
