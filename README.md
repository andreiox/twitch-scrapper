# twitch-scrapper

## **Description**

Get most viewed clips on twitch and downloads them

## **Installation**

**Passo 1** - Create a virtualenv

```shell
virtualenv --python=/usr/local/bin/python3.6 venv
```

**Passo 2** - Activate the virtualenv

```shell
source venv/bin/activate
```

**Passo 3** - Install dependencies via requirements.txt

```shell
pip install -r requirements.txt
```

## **Running**

```shell
source venv/bin/activate
python main.py [period] [language]
```

Values for **period**: day, week, month, all

Some values for **language**: en, es, th

## **Example response**

```json
[
  {
    "streamer": "xQcOW",
    "game": "Just Chatting",
    "views": 68966,
    "duration": 53.75,
    "clip_url": "https://clips-media-assets2.twitch.tv/AT-cm%7C471336223.mp4",
    "clip_path": "/home/andre/@/clips/AT-cm%7C471336223.mp4"
  },
  {
    "streamer": "Trainwreckstv",
    "game": "Just Chatting",
    "views": 68685,
    "duration": 26,
    "clip_url": "https://clips-media-assets2.twitch.tv/34435056512-offset-20324.mp4",
    "clip_path": "/home/andre/@/clips/34435056512-offset-20324.mp4"
  },
  {
    "streamer": "MethodJosh",
    "game": "World of Warcraft",
    "views": 66169,
    "duration": 10.65,
    "clip_url": "https://clips-media-assets2.twitch.tv/AT-cm%7C471227259.mp4",
    "clip_path": "/home/andre/@/clips/AT-cm%7C471227259.mp4"
  }
]
```

## **References**

- [Twitch API Documentation](https://dev.twitch.tv/docs/v5/reference/clips/#get-top-clips)
