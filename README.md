# twitch-scrapper

## **Descrição**

Esse cara é responsável por varrer a twitch, pegar os clips mais assistidos e fazer download dos mesmos.

## **Instalação**

**Passo 1** - Crie um virtualenv com python 3.6

```shell
virtualenv --python=/usr/local/bin/python3.6 venv
```

**Passo 2** - Ative o virtualenv criado

```shell
source venv/bin/activate
```

**Passo 3** - Instale as dependencias via o arquivo requirements.txt

```shell
pip install -r requirements.txt
```

## **Rodando o carinha**

```shell
source venv/bin/activate
python main.py [period] [language]
```

Valores possíveis para **period**: day, week, month, all

Alguns valores para **language**: en, es, th

## **Exemplo json gerado**

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

## **Referências**

- [Documentação Twitch API](https://dev.twitch.tv/docs/v5/reference/clips/#get-top-clips)
