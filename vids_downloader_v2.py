from pytube import YouTube
import shutil
import ffmpeg
import os
#itag for 4k = 313
#itag for FHD = 137
#itag for HD = 22
#itag for 720p = 22
#itag for 480p = 135
#itag for 360p = 133
#itag for 240p = 18
#itag for audio = 251

url = input("\nPlease, enter the video's URL here: ")
choose_q = input("[4K], [FHD], [HD], [480p], [360p] or [240p]: ").lower()

loaded_url = YouTube(url)
v_title = loaded_url.title

valid_v_title = v_title
remove_character = ["/","\\" , ":", "|" , "," , ">"]
try:
    for char in remove_character:
        valid_v_title = v_title.replace(remove_character, '')
except:
    valid_v_title

d_audio = loaded_url.streams.get_by_itag(251)
d_audio.download()
audio_name = os.rename(valid_v_title + '.webm', 'Downloaded_audio.webm')

print('*' * 15, '\nAudio downloaded successfully\nDownloading Video...\n,'*' * 15')

def down_4k():
    d_video = loaded_url.streams.get_by_itag(313).download()
    #NB: 4K videos has a .webm extension UNLIKE other formats ending in .mp4
    video_name = os.rename(x + '.webm', 'Downloaded_video.webm')

def down_fhd():
    d_video = loaded_url.streams.get_by_itag(137).download()

def down_hd():
    d_video = loaded_url.streams.get_by_itag(22).download()
    #NB: 4K videos has a .webm extension UNLIKE other formats ending in .mp4
    video_name = os.rename(x + '.mp4', 'Downloaded_video.mp4')

def down_480p():
    d_video = loaded_url.streams.get_by_itag(135).download()
    video_name = os.rename(x + '.mp4', 'Downloaded_video.mp4')

def down_360p():
    d_video = loaded_url.streams.get_by_itag(133).download()
    video_name = os.rename(x + '.mp4', 'Downloaded_video.mp4')

def down_240p():
    d_video = loaded_url.streams.get_by_itag(18).download()
    video_name = os.rename(x + '.mp4', 'Downloaded_video.mp4')
print("Downloading " + loaded_url.title)
if choose_q == '4k':
    try:
        down_4k()
    except:
        pass
        try:
            down_fhd()
        except:
            pass
            try:
                down_hd()
            except:
                pass
                try:
                    down_480p()
                except:
                    pass
                    try:
                        down_360p()
                    except:
                        down_240p()

if choose_q == 'fhd':
    try:
        down_fhd()
    except:
        pass
        try:
            down_hd()
        except:
            pass
            try:
                down_480p()
            except:
                pass
                try:
                    down_360p()
                except:
                    down_240p()

if choose_q == 'hd':
    try:
        down_hd()
    except:
        pass
        try:
            down_480p()
        except:
            pass
            try:
                down_360p()
            except:
                down_240p()

if choose_q == '480p':
    try:
        down_480p()
    except:
        pass
        try:
            down_360p()
        except:
            down_240p()

if choose_q == '360p':
    try:
        down_360p()
    except:
        down_240p()

if choose_q == '240p':
    down_240p()

#put the video and audio into ffmpeg
video = ffmpeg.input('Downloaded_video.mp4')
audio = ffmpeg.input('Downloaded_audio.webm')

out = ffmpeg.output(video, audio, r'E:\\Programming\\Python\\yt_vids_download\\final.mp4', vcodec='copy')
out.run()

os.mkdir(valid_v_title)
shutil.move('Downloaded_video.mp4',valid_v_title)
shutil.move('Downloaded_audio.webm', valid_v_title)
shutil.move('final.mp4', valid_v_title)

os.chdir(valid_v_title)
os.rename('final.mp4', x + '.mp4')
os.remove('Downloaded_video.mp4')
os.remove('Downloaded_audio.webm')
os.startfile(valid_v_title + '.mp4')
print('\n',' *' * 15, '\n Video Downloaded Successfully.\n',' *' * 15)