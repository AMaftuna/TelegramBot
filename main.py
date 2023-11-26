import telebot
import configure
from commands import client
from database import create_tables

create_tables()

client.polling(none_stop=True,interval=0)
