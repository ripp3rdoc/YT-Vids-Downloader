import pafy

url = input("Please, enter YT video link: ")
video = pafy.new(url)
stream = video.allstreams
stream_count = 0
#listing the qualities available
for i in stream: 
    print("Quality (",int(stream_count),")",i)
    stream_count += 1
quality = int(input("Choose the resolution of the video (To get the best resolution type '99'): "))
print("Getting content...")
if quality == 99:
    #gets the best resolution of the video
    video.getbest().download()
else:
    #gets any other choosen quality
    stream[int(quality)].download()
print("\n\n**Download has finished.**\n\n**If you got a problem downloading a choosen quality; try getting the best (99)**")