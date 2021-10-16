from telegram.ext import *
import requests

app_id ="VUVX4Q-47T2W8PVHV"

def wolf(update, ctx):

    initial_query = update.message.text
    query = initial_query.replace("/wolf ", "")
    print(query)

    
   
    url= f"https://api.wolframalpha.com/v1/result?appid={app_id}&i={query}%3F"

    response = requests.get(url)
    update.message.reply_text(f"RESULTS: \n \n {response.text}")

