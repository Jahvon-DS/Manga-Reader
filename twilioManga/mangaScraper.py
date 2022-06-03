from asyncio.windows_events import NULL
from base64 import decode
#from crypt import methods
from email import message
from http import client
from requests import request
import requests
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
import urllib3
import keys
from bs4 import BeautifulSoup 
from urllib.request import urlopen, Request
from flask import *
import requests
import codecs

app = Flask("MangaScraper")



@app.route("/manga", methods=["POST", "GET"])
def manga():

 requestManga = request.values.get('Body', '')
  
  
# requestManga = input("Please Enter Manga:")



 url = "https://readmangafull.com/" + requestManga.replace(" ", "-").replace("&", "/").lower() + "/all-pages"
 #print(url)

 head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'} 
 #PARAMS = {'headers':head}
 #UserAgent = Request("https://read-manga.org/black-clover/chapter-331/all-pages",headers=head)
 UserAgent= requests(url,headers=head)
 
    
 #UserAgent= Request(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'})
 page = urlopen(UserAgent)
 html = page.read().decode("utf-8")
 soup = BeautifulSoup(html, "html.parser")

#specifying which type of images to take
 images = soup.select('img[src ^="https://readm.org//uploads/chapter_files/"]')
 client = Client(keys.account_sid,keys.auth_token)
 
 resp= MessagingResponse()
 msg = resp.message()
 pages = {}

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


'''
#making request via twilio 
client = Client(keys.account_sid,keys.auth_token)

#sending the images to twilio phone number
for i in images: 
   print( client.messages.create(body = 'This is a page from manga', media_url= i ['src'], from_ = keys.twilio_number, to = keys.my_phone_number ))

'''




'''
mangaName = input(client.messages.create( 
    body= 'This is a page from manga:',
    media_url= [url_mangaChapter['src']],
    from_ = keys.twilio_number,
    to =keys.my_phone_number
))

## printing this to the device --> will need to iterate

'''
















'''
app = Flask("MangaScraper")



@app.route("/manga", methods=["POST", "GET"])
def manga():
  if request.method == 'POST': 
    mangaName = urllib3.parse.quote(request.form['Body'])
    url = "https://readmangafull.com" + mangaName.replace(" ", "-")

    MessagingResponse().message("What Chapter?")
    mangaChapter = request.values.get('Body', '')

    url_mangaChapter = str(url + "/chapter-" + str(mangaChapter) + "/all-pages")

    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'} 
    PARAMS = {'header':head}
    UserAgent= Request(url_mangaChapter,PARAMS)
     
    
     #UserAgent= Request(url_mangaChapter,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'})
    page = urlopen(UserAgent)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

#specifying which type of images to take
    images = soup.select('img[src ^="https://readm.org//uploads/chapter_files/"]')

    def pages():
      for i in images: 
        print(i['src'])
    return pages
'''