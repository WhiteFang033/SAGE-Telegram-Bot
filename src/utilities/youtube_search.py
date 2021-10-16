from telegram.ext import *
import requests
import json


def youtube_search(update, ctx):
   url = "https://youtube-search-results.p.rapidapi.com/youtube-search/"
    
   initial_keyword = update.message.text
   keyword = initial_keyword.replace("/yt", "")

   querystring = {"q":keyword}

   headers = {
    'x-rapidapi-host': "youtube-search-results.p.rapidapi.com",
    'x-rapidapi-key': "a7202c6505mshac4812d4e1434b3p1e7c3bjsn26341f464af9"
       }

   response = requests.get( url, headers=headers, params=querystring)
   data = json.loads(response.text)
   items= data["items"]
   link = items[0]["url"]

   update.message.reply_text(link)