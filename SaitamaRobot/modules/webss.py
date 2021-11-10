from SaitamaRobot import pbot
from pyrogram import filters 
import requests
import os

@pbot.on_message(filters.command("webss"))
def webss(_,message):
   site = message.text.replace(message.text.split(' ')[0], '')
   res = requests.get("https://webshot.amanoteam.com/print?q={}".format(site)).content
   with open("webss.jpg" ,"wb") as f:
        f.write(res)
   pbot.send_photo(message.chat.id , "webss.jpg")
   os.remove("webss.jpg")
