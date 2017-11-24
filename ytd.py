from __future__ import unicode_literals
import youtube_dl


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print(' Almost done')
    if d['status'] == 'error':
        print('Error in downloading the video')


ydl_opts = {
    'format': 'bestvideo+bestaudio/best',
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}

def download_video(link):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(link)