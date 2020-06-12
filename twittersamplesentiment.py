import os
import requests
import json
from pprint import pprint
from requests.auth import AuthBase
import boto3
from requests.auth import HTTPBasicAuth

consumer_key = "" # Add your API key here
consumer_secret = "" # Add your API secret key here

stream_url = "https://api.twitter.com/labs/1/tweets/stream/sample"

comprehend = boto3.client(service_name= 'comprehend', aws_access_key_id= 'aws_access_key_id',
                          aws_secret_access_key = 'aws_secret_access_key', region_name = 'region_name')

# Gets a bearer token
class BearerTokenAuth(AuthBase):
  def __init__(self, consumer_key, consumer_secret):
    self.bearer_token_url = "https://api.twitter.com/oauth2/token"
    self.consumer_key = consumer_key
    self.consumer_secret = consumer_secret
    self.bearer_token = self.get_bearer_token()

  def get_bearer_token(self):
    response = requests.post(
      self.bearer_token_url,
      auth=(self.consumer_key, self.consumer_secret),
      data={'grant_type': 'client_credentials'},
      headers={"User-Agent": "TwitterDevSampledStreamQuickStartPython"})

    if response.status_code != 200:
      raise Exception(f"Cannot get a Bearer token (HTTP %d): %s" % (response.status_code, response.text))

    body = response.json()
    return body['access_token']

  def __call__(self, r):
    r.headers['Authorization'] = f"Bearer %s" % self.bearer_token
    return r

def stream_connect(auth):
  response = requests.get(stream_url, auth=auth, headers={"User-Agent": "TwitterDevSampledStreamQuickStartPython"}, stream=True)
  for response_line in response.iter_lines():
    if response_line:
      tweet = json.loads(response_line)
      text = tweet['data']['text']
      pprint(tweet['data']['id'])
      pprint(comprehend.detect_sentiment(Text = text, LanguageCode='en')['Sentiment'])
      pprint("------------------------")

bearer_token = BearerTokenAuth(consumer_key, consumer_secret)

# Listen to the stream. This reconnection logic will attempt to reconnect as soon as a disconnection is detected.
while True:
  stream_connect(bearer_token)