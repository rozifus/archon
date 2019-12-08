
# Archon

A basic setup for youtube-dl with python

## Setup
(ideally use a virtual environment / venv)

```
pip install youtube-dl
```

Add some channels / videos/ usernames to `youtube` list in `_example_config.py` and rename to `config.py`

Use `media` string to select whether to trigger download of ('v')video-with-audio and/or ('a')audio-only

``` python
# eg.
[
    [
        'https://www.youtube.com/channel/yasdkjfasjdfjkls',  # channel url
        'ChannelAlias',                                      # channel alias / save folder
        'va',                                                # save video-with-audio + audio-only files
    ],
    [
        'SomeChannelName',  # channel name
        None,               # use channel name as alias
        'v'                 # save video-with-audio file
    ],
]

```

## Run Archon

```
python archon.py
```

# Purge Duplicates

Removes older versions of video files that have the same name and almost identical file sizes

## Setup

```
pip install pymediainfo
pip install recordtype
```

## Run Purge Duplicates

```
python purge-duplicates.py
```


