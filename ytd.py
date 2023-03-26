import sys
import os
from pathlib import Path
from pytube import YouTube

link = ""
filename = ""
path = f"{Path.home()}\\Downloads\\"

try:
  link = sys.argv[1]
  print(f"Link: {sys.argv[1]}")
except:
  link = input("Link: ")

youtube = YouTube(link)

try:
  filename = sys.argv[2]
  print(f"Filename: {sys.argv[2]}")
except:
  if input(f"Filename auto? ({youtube.title}.mp4) [Y/n] ") in ["y", "Y", ""]:
    print("Yes")
    filename = f"{youtube.title}.mp4"
  else:
    filename = input("Enter filename: ")
    if not ".mp4" in filename:
      filename += ".mp4"


if input(f"Save path auto? ({path}) [Y/n] ") in ["y", "Y", ""]:
  print("Yes")
else:
  path = input("Enter save path: ")
  if not path.endswith("\\"):
    path += "\\"

print("Available resolutions: ")

streams = youtube.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')
resolutions = map(lambda x: x.resolution, streams)

for i, res in enumerate(resolutions):
  print(f"{i}. {res}")

print("Choose resolution (by number): ", end="")
if "1080p" in resolutions:
  print("(1080p default)", end="")

chosenResNum = input()

if chosenResNum == "" and "1080p" in resolutions:
  stream = streams[resolutions.index("1080p")]
else:
  stream = streams[int(chosenResNum)]

print("Downloading...")

stream.download(output_path = path)

print(f"Downloaded {filename} into {path}")

os.rename(path + youtube.title + ".mp4", path + filename)
