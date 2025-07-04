#!/usr/bin/python
import e621py_wrapper as e621
import requests
import json
import os
import time


client = e621.client()
# Put your user name in the first parameter, and your API key in the 2nd
client.login("username here", "API key here")

# the amounts of images Max: 100
search_limit = 200

# file operations
dir_path = os.path.dirname(os.path.realpath(__file__))
image_path = os.path.join(dir_path, "images")
new_file = os.path.join(image_path, 'search.json')
file_name = 'search.json'

os.chdir(dir_path)
#bot = telebot.TeleBot('6603476753:AAHNg-7Ggt3vDIBhTqFvGClxNwzvIYR92I8')

# Determines the time to cycle images
time_to_delete = time.time() - 20

# Creates the image folder in the cwd
if not os.path.isdir(image_path):
    os.mkdir(image_path)

# User input for tags to search for
#tag = input("search for a tag: ")

# gets the json data from e621
# 1st param is tags
# 2nd is blacklists
data = client.posts.search(f" rating:s order:random status:active -macro -diaper -feral -human -dbz -mpreg -sega", "rating:e rating:q underage cub vore fart", search_limit)

# changes to the cwd
os.chdir(image_path)

# Deletes the entire directory when running it

def create_json_file():

    if os.path.isfile('search.json'):
        print('ok')
        os.remove('search.json')

    try:
        with open(file_name, 'r+') as f:
            json.dump(data, f, indent=4)
            f.close()
    except FileNotFoundError:
        with open(new_file, 'w') as f:
            json.dump(data, f, indent=4)
            f.close()
    fetch_images()


def fetch_images():
    os.chdir(image_path)
    for js_data in data:
        url = js_data['file']['url']
        id = js_data['id']
        img_dl = requests.get(url).content
        print(id)
        if f"{id}.webm" in os.listdir() or f"{id}.gif" in os.listdir():
            print('file already exists, skipping...')
        elif "jpg" in url:
            print('jpg ok...')
            f = open(f"{id}.jpg", 'wb')
            f.write(img_dl)
            f.close()
        elif "png" in url:
            print('png ok...')
            f = open(f"{id}.png", 'wb')
            f.write(img_dl)
            f.close()
        elif "gif" in url:
            print('gif ok...')
            f = open(f"{id}.gif", 'wb')
            f.write(img_dl)
            f.close()
        elif "webm" in url:
            print('webm ok...')
            f = open(f"{id}.webm", 'wb')
            f.write(img_dl)
            f.close()

create_json_file()
