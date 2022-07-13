import os 

app_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig():
    DEBUG = True
    SECRET_KEY = '2e846f708d6baa034912bfd7e43851ded69e481e61d23bac12be8cadf51cdd7f0d9bbe36144f22c46d85a21796739b1279f92a07ff3e148cc00b9b4e4de2caf4'
    SQLALCHEMY_DATABASE_URI = os.path.join(app_dir, 'bot.db')
    SQLALCHEMY_MIGRATE_REPO = os.path.join(app_dir, 'bot_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False