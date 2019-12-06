import os

class Config:
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	UPLOADED_PHOTOS_DEST ='app/static/photos'
	SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:tracy:Wakanda2030@localhost/book'
	SECRET_KEY = os.environ.get('SECRET_KEY')
	# mail configurations
	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
	MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

	@staticmethod
	def init_app(app):
		pass

class TestConfig(object):
	"""docstring for TestConfig."""

	SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Jacques@localhost/bookstore_test'

class ProdConfig(Config):

	SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
	SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://tracy:Wakanda2030@localhost/book'

	DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}