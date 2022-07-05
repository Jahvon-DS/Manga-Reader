
from requests import request
import requests
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
import keys
from bs4 import BeautifulSoup 
from flask import *
import requests


app = Flask("MangaScraper")
 
 
 
@app.route("/manga", methods=["POST", "GET"])
def manga():
 
 requestManga = request.values.get('Body', '') 
 #recvieving input from the user
 
  
 url = "https://readmangafull.com/" + requestManga.replace(" ", "-").replace("&", "/").lower() + "/all-pages"
#creating a url link based on the user input
 
 head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'}  
 UserAgent= requests.request("GET",url,headers=head)
 #creating the request to the site
 
 soup = BeautifulSoup(UserAgent.text, "html.parser")
 
#specifying which type of images to take
 images = soup.select('img[src ^="https://readm.org//uploads/chapter_files/"]')

 client = Client(keys.account_sid,keys.auth_token)
 
 resp= MessagingResponse()
 msg = resp.message()


 
 
 '''    
for i in images:
  global pages
  pages = []
# print( client.messages.create(body = 'This is a page from manga', media_url= i ['src'], from_ = keys.twilio_number, to = keys.my_phone_number ))
return pages.append(i['src'])
 
       '''
       
 for i in images:
  resp.message( client.messages.create(body = 'This is a page from manga', media_url= i ['src'], from_ = keys.twilio_number, to = keys.my_phone_number ))
 
 return str(resp)
 
app.run()

