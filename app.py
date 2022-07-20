from flask import Flask
from config import BaseConfig, RedisConfig, TelegramConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from redis import Redis
from services.telegram_api import TelegramApi
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker

app= Flask(__name__)
app.config.from_object(BaseConfig)

#db=SQLAlchemy(app)

#migrate=Migrate(app,db)

# manager = Manager(app)
# manager.add_command('db',MigrateCommand)

redis = Redis(host = RedisConfig.HOST, port = RedisConfig.PORT, db = RedisConfig.DB )

api_bot = TelegramApi(TelegramConfig.TOKEN)


engine = create_async_engine(BaseConfig.SQLALCHEMY_DATABASE_URI, future=True, echo=True)
async_session = sessionmaker(engine, expire_on_commit=False, class_= AsyncSession)
Base = declarative_base()