# Provides a portable way of using operating system dependent functionality
import os 
# Access to Twitter API
import tweepy 
# Allows you to send HTTP requests
import requests
# Offers a number of high-level operations on files and collections of files, includign  file copying and removal.
import shutil
# Randomness, plain and simple.
import random

# lines: 13 - 21, Creating variables and assigning Keys, Tokens, and Secrets to them for passing. V2 and V1 options included. It's worth noting that these are formatted for Google Cloud. If testing locally, simply pass your credentials to the r espective variable.
api_key = os.environ.get('Api_key')
api_secret = os.environ.get('Api_secret')
bearer_token = os.environ.get('Bearer_token')
access_token = os.environ.get('Access_token')
access_token_secret = os.environ.get('Access_token_secret')
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
client = tweepy.Client(bearer_token, api_key, api_secret, access_token,access_token_secret)

# Defining the function "tweetToSend". Arguments are needed for Scheduling via Google Cloud.
def tweetToSend(event, context):
    # Creating a variable called "cardIds", and having it pull a random integer          between the specified range of 0 - 4980.
    cardIds = random.randint(0, 4980)
    # Creating variable "response", that pulls a random card through API using a r       andomised multiverse ID. This multiverse ID it tacked on to a specific URL           endpoint, and generated through the "cardIDs" variable.
    response = requests.get('https://api.scryfall.com/cards/multiverse/' + str(cardIds))
    # Creating variable "m". This variable takes our "response", and returns it as        Json encoded content.
    m = response.json()
    # Creating variable "url". This variable takes "m", and grabs the a specific         key: value from the endpoint. In this specific instance we've generated a            specific card through "response", and through "url" have grabbed the respective      card's image url key (image_uris) and then a specified image URL value (normal).     This value has the card image, which we'll be posting.
    url = (m["image_uris"]["normal"])
  
    # Creating variable "res", and assigning "url" to it.
    res = requests.get(url, stream=True)
    # If "res" can be grabbed successfully:
    if res.status_code == 200:
      # Open local tmp directory and upload image (res) to said tmp directory.
      with open('/tmp/mtgCard.jpg', 'wb') as f:
        shutil.copyfileobj(res.raw, f)

    # If successful, create variable "media", and try to upload image to twitter.
    try:
      media = api.media_upload('/tmp/mtgCard.jpg')
      client.create_tweet(media_ids=[media.media_id_string])

    # Otherwise, print given error.
    except Exception as error:
      print(error)