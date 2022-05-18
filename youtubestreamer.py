from threading import Thread
import vlc

import pafy, time
from youtubesearchpython import VideosSearch
import random

class Streamer:
    def __init__(self):
        self.__url = None  # url that will be played
        self.media = None  # VLC media player instance
        self.loaded = False  # variable to check if a url was loaded
        self.playing = False  # variable to stop the vlc.play() thread
    
    def get_urls(self, keyword:str, limit:int=10):
        """Reads the first 10 videos given by youtube when searching for something.

        Args:
            keyword (str): What to search for.
            limit (int, optional): How many video urls should be returned (max). Defaults to 10.

        Returns:
            list: A list of urls corresponding to the videos.
        """
        
        results = VideosSearch(keyword, limit=limit).result()["result"]
        urls = []
        for i in results:
            urls.append(i["link"])
            # video title is in i["title"]
        return urls
    
    def set_aktual_url(self, url:str):
        """Set the class' url to url (if you don't want to create a variable 
        you use only once).

        Args:
            url (str): A url to the desired youtube video.
        """
        
        self.__url = url
        self.loaded = False
    
    def load_audio(self, url:str=None):
        """Loads audio from a url to the vlc Media Player.

        Args:
            url (str, optional): Url to load. Defaults to None and is the url 
            defined in set_aktual_url if not changed.
        """
        
        if not url:
            url = self.__url
        video = pafy.new(url)
        best_audio = video.getbestaudio()
        self.media = vlc.MediaPlayer(best_audio.url)
        self.loaded = True
    
    def __play(self):
        """Starts to play the audio. Usually launched in a thread.
        """
        
        self.media.play()
        while self.playing:
            time.sleep(0.1)

    def play(self, url:str=None):
        """Play the audio.

        Args:
            url (str, optional): Url to the video. Defaults to None.
        """
        
        if url:
            self.__url = url
            self.load_audio()
        if not self.loaded:
            self.load_audio()
        
        self.playing = True
        thread = Thread(target=self.__play)
        thread.start()
    
    def pause(self):
        """Pause playing audio.
        """
        
        self.media.pause()
    
    def stop(self):
        """Stop audio and thread.
        """
        self.playing = False
        self.media.stop()

        
if __name__ == "__main__":
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
