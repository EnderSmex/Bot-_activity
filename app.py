from flask import Flask
from config import BaseConfig, RedisConfig, TelegramConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from redis import Redis
from services.telegram_api import TelegramApi

app= Flask(__name__)
app.config.from_object(BaseConfig)

db=SQLAlchemy(app)

migrate=Migrate(app,db)

manager = Manager(app)
manager.add_command('db',MigrateCommand)

redis = Redis(host = RedisConfig.HOST, port = RedisConfig.PORT, db = RedisConfig.DB )

api_bot = TelegramApi(TelegramConfig.TOKEN)


