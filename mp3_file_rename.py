import os
from mutagen.mp3 import MP3  
from mutagen.easyid3 import EasyID3  
import mutagen.id3  
from mutagen.id3 import ID3, TIT2, TIT3, TALB, TPE1, TRCK, TYER  
import glob  

# dir_path = r'F:\\ProgramData\\ABLETON_MEDIA\\Ableton Renders\\spotify_recorder\\Liked_Songs_11092022'
dir_path = f"E:\\Audio_temp\\Spotify_221022"

res = []

for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)):
        res.append(path)

for file_name in res:
    mp3file = MP3(f"{dir_path}\\{file_name}", ID3=EasyID3) 
    artist = file_name.split(" - ").pop().split(".mp3",1)[0]
    title = file_name.split(" - ")[:-1]
    title = ' - '.join(title)
    mp3file["artist"] = [f"{artist}"]  
    mp3file["title"] = [f"{title}"] 
    mp3file.save()   



