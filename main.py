import os
import sys
import json
import requests

from dotenv import load_dotenv


load_dotenv()

URL_TOP_CLIPS = 'https://api.twitch.tv/kraken/clips/top'


def main():
    response = get_clips_from_twitch()

    clips = []
    for clip in response['clips']:
        clips.append(format_clip(clip))

    make_request_to_video_guy(clips)
    print('Im done!')


def get_clips_from_twitch():
    period = str(sys.argv[1])
    language = str(sys.argv[2])

    params = {'period': period, 'limit': os.getenv('QUERY_LIMIT'), 'language': language}
    headers = {'Accept': 'application/vnd.twitchtv.v5+json', 'Client-ID': os.getenv('CLIENT_ID')}

    r = requests.get(URL_TOP_CLIPS, params=params, headers=headers)
    return r.json()


def format_clip(clip):
    thumbnail_url = clip['thumbnails']['tiny']
    clip_url = thumbnail_url[:(thumbnail_url.index('preview') - 1)] + '.mp4'

    formated_clip = {
        'streamer': clip['broadcaster']['display_name'],
        'game': clip['game'],
        'views': clip['views'],
        'duration': clip['duration'],
        'clip_url': clip_url,
        'clip_path': os.getenv('CLIPS_FOLDER') + clip_url[clip_url.rfind('/'):]
    }

    download_video(formated_clip['clip_url'], formated_clip['clip_path'])

    return formated_clip


def download_video(url, output_filename):
    video_stream = requests.get(url, stream=True)
    with open(output_filename, "wb") as writer:
        writer.write(video_stream.content)


def make_request_to_video_guy(clips):
    raise NotImplementedError


if __name__ == "__main__":
    main()
