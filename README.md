# Simple Youtube Streamer
Play youtube audio using your code without downloading it.

Prerequisites:
* VLC media player
* python-vlc (`pip3 install python-vlc`)
* youtube-dl (`pip3 install youtube-dl`)
* pafy (`pip3 install pafy`)
* youtubesearchpython (`youtube-search-python`)
#### Example
```
from youtubestreamer import Streamer

s = Streamer()

keyword = input("Keyword: ")

urls = s.get_urls(keyword)
s.set_aktual_url(urls[0])
s.play()

a = None

while a != "s":
    a = input("Action: ")
    if a == "p":
        print("pausing")
        s.pause()

s.stop()
```

Code of the `Streamer` - class is self explanatory (i hope), read it to learn more.
Feel free to ask if there are questions, and please tell me if there are any bugs.
