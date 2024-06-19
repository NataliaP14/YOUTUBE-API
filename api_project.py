import requests
import googleapiclient.discovery
import os
import pprint


YOUTUBE_API = os.environ.get('API_KEY')
api_service_name = "youtube"
api_version = "v3"

def channel_id(name):
  
  youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=YOUTUBE_API)

  request = youtube.channels().list(
    part='id',
    forUsername=name
  )

  response = request.execute()

  return response['items'][0]['id']

def get_5_videos(id, results=5):
  youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=YOUTUBE_API)

  request = youtube.search().list(
    part='snippet',
    channelId = id,
    type='video',
    maxResults=results
  )

  response = request.execute()

  print("Five Videos of " + response['items'][0]['snippet']['channelTitle'] + '\n')

  for item in response['items']:
    print('Title: ' + item['snippet']['title'])
    print('Published at: ' + item['snippet']['publishedAt'])
    print('Link: ' + 'https://www.youtube.com/watch?v=' + item['id']['videoId'] + '\n')
    






if __name__ == '__main__':
  user_input = input("Enter a youtube channel, without spaces ")
  id = channel_id(user_input)
  if id:
    get_5_videos(id)