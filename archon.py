from __future__ import unicode_literals
import youtube_dl
import config
import os
import os.path
import thumbs


BASE_ARCHIVE_PATH = os.path.join(os.getcwd(), "saved")

class MyLogger(object):
    def debug(self, msg):
        print(msg)

    def warning(self, msg):
        print(msg)

    def error(self, msg):
        print(msg)

global_opts = {
        'ignoreerrors': True,
        'writethumbnail': True,
        'updatetime': False,
        'logger': MyLogger(),
}

VIDEO_FILENAME = '%(title)s.%(ext)s'
AUDIO_FILENAME = '(audio) %(title)s.%(ext)s'

def download_audio():
    for source, alias, options in config.youtube:
        if alias == None:
            alias = source
            source = 'ytuser:' + username

        if 'a' in options.lower():
            opts = global_opts.copy()
            opts['outtmpl'] = os.path.join(BASE_ARCHIVE_PATH, 'youtube', alias, 'audio', AUDIO_FILENAME)
            opts['format'] = 'bestaudio'
        with youtube_dl.YoutubeDL(opts) as yd:
            yd.download([source])

def download_video():
    for source, alias, options in config.youtube:
        if alias == None:
            alias = source
            source = 'ytuser:' + username

        if 'v' in options.lower():
            opts = global_opts.copy()
            opts['outtmpl'] = os.path.join(BASE_ARCHIVE_PATH, 'youtube', alias, VIDEO_FILENAME)
        with youtube_dl.YoutubeDL(opts) as yd:
            yd.download([source])

media_operations = {
    'a': download_audio,
    'v': download_video
}

for letter in config.media:
    if letter.lower() in media_operations.keys():
        media_operations[letter.lower()]()

thumbs.tidy(os.getcwd())
