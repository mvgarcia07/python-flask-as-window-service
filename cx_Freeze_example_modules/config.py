import os
#from dotenv import load_dotenv
#basedir = os.path.abspath(os.path.dirname(__file__))
#load_dotenv(basedir, ".env")


class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY')

	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG = True
	DATA_DIR_INPUT_FILE = os.environ.get('DATA_DIR_INPUT_FILE')



config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}