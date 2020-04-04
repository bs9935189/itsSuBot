from telethon.sync import TelegramClient
from telethon.sessions import StringSession

print("""Please go-to my.telegram.org
Login using your Telegram account
Click on API Development Tools
Create a new application, by entering the required details""")

API_KEY = input("1309461: ")
API_HASH = input("4e3c7ed9288d1e2b45fc75723e2a9484: ")

with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
    print("Here is your userbot srting, copy it to a safe place !!")
    print("")
    print(client.session.save())
    print("")
    print("")
    print("Enjoy your userbot !!")
