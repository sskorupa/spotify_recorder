import eyed3
import os

dir_path = r'F:\\ProgramData\\ABLETON_MEDIA\\Ableton Renders\\spotify_recorder\\Liked_Songs_11092022'

res = []

for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)):
        res.append(path)

for file_name in res:
    audiofile = eyed3.load(f"{dir_path}\\{file_name}")
    audiofile.tag.artist = file_name.split(" - ").pop().split(".mp3",1)[0]
    title = file_name.split(" - ")[:-1]
    title = ' - '.join(title)
    audiofile.tag.title = title
    audiofile.tag.save()



