import googleapiclient.discovery
import os
import sqlalchemy as db
import pandas as pd
from flask import Flask, render_template, url_for, flash, redirect, request


YOUTUBE_API = os.environ.get('API_KEY')
api_service_name = "youtube"
api_version = "v3"


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default_secret_key')


def channel_id(name):

    youtube = googleapiclient.discovery.build(
      api_service_name, api_version, developerKey=YOUTUBE_API
    )

    request = youtube.channels().list(
      part='id',
      forUsername=name
    )

    response = request.execute()

    if 'items' in response and response['items']:
        return response['items'][0]['id']
    else:
        print(f'No channel found for {name}')
        return None


def get_5_videos(id, results=5):

    youtube = googleapiclient.discovery.build(
      api_service_name, api_version, developerKey=YOUTUBE_API
    )

    request = youtube.search().list(
      part='snippet',
      channelId=id,
      type='video',
      maxResults=results
    )

    response = request.execute()

    videos = []
    for item in response['items']:
        data = {
          'Title': item['snippet']['title'],
          'Published at': item['snippet']['publishedAt'],
          'Link': 'https://www.youtube.com/watch?v=' + item['id']['videoId']
        }
        videos.append(data)

    return videos


@app.route("/", methods=['GET', 'POST'])
def database_to_index():
  if request.method == 'POST':
    input = request.form['channel_name']
    id = channel_id(input)
    if id:
        videos = get_5_videos(id)
        videos_df = pd.DataFrame.from_dict(videos)

        engine = db.create_engine('sqlite:///youtube_api.db')

        if not videos_df.empty:
            videos_df.to_sql(
              'video', con=engine, if_exists='replace', index=False
            )

            with engine.connect() as connection:
                query_result = connection.execute(
                      db.text("SELECT * FROM video;")
                ).fetchall()
                result = pd.DataFrame(query_result, columns=['Title', 'Published at', 'Link'])
                return render_template("index.html", tables=[result.to_html(classes='data')], titles=result.columns.values)
        else:
            return render_template("index.html", error = "No videos found for this channel!")
    else:
        return render_template("index.html", error = "No valid ID!")
  return render_template("index.html")



if __name__ == '__main__':
  app.run(debug=True, host="0.0.0.0")
    
