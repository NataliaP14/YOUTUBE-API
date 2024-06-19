import requests
import googleapiclient.discovery
import os


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

  return response

def top_5_videos(id, results=5):
  youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=YOUTUBE_API)

  request = youtube.channels().list(
    
  )






if __name__ == '__main__':
  user_input = input("Enter a youtube channel, without spaces ")
  id = channel_id(user_input)
  top_5_videos(id)