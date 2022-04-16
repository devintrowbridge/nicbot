import json
from urllib import parse, request
import random
import os

from dotenv import load_dotenv
load_dotenv()
GIPHY_API = os.getenv('GIPHY_API')

url = "http://api.giphy.com/v1/gifs/search"

def get_nicgif():
  random.randint(0, 4999)

  params = parse.urlencode({
    "q": "nic cage",
    "api_key": GIPHY_API,
    "limit": "1",
    "offset": str(random.randint(0, 100))
  })

  with request.urlopen("".join((url, "?", params))) as response:
    data = json.loads(response.read())
  return data['data'][0]['embed_url']