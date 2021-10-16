from telegram.ext import *
import requests
import json


def youtube_search(update, ctx):
   url = "https://youtube-search-results.p.rapidapi.com/youtube-search/"
    
   initial_keyword = update.message.text
   keyword = initial_keyword.replace("/yt", "")

   querystring = {"q":keyword}

   headers = {
    'x-rapidapi-host': "API HOST URL",
    'x-rapidapi-key': "YOUR API KEY HERE"
       }

   response = requests.get( url, headers=headers, params=querystring)
   data = json.loads(response.text)
   items= data["items"]
   link = items[0]["url"]

   update.message.reply_text(link)
