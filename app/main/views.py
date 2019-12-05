import os
from flask import render_template,request,redirect,url_for
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename

from . import main
from .. import db
from .forms import BookForm
from ..models import User, Books
from .. import create_app

# Views
@main.route('/')
def index():
	title = 'Book Club'
	return render_template('index.html',title = title)

@main.route('/bookupload', methods = ['GET', 'POST'])
# @login_required
def book():
	title = 'Book Club'
	form = BookForm()
	if form.validate_on_submit():
		title = form.title.data
		author = form.title.data
		description = form.description.data

		photo = form.upload.data
		filename = secure_filename(photo.filename)
		photo.save(os.path.join(
			app.instance_path, 'photos', filename
		))

		new_book = Books(title = title , author = author, description = description, user = current_user,photo = photo)
		new_book.save_book()
		return redirect(url_for('.index'))

	return render_template('book.html', title = title, book_form = form)

@main.route('/archives')
def archives():

	return render_template('archives.html')

@main.route('/specificbook')
def specific():
	return render_template('specificbook.html')
