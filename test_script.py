#!/usr/bin/env python3
from e621 import E621
import requests

USER_AGENT = "MyApp/1.0 (by Scrublord on e621)"
USERNAME = "Scrublord"
API_KEY = "ktXhuzqcjuwukkdUmCU7uMQD"

# Force tuple to avoid string interpretation
auth = (USERNAME, API_KEY)

# Ensure E621 client receives exactly 2 items to unpack
api = E621(auth)
posts = api.posts.search(["canine", "-3d"])
try:
    posts = api.posts.search(["canine", "-3d"])
    print(posts)
    for post in posts:
    	print(post.score.total, post.all_tags, post.relationships.parent_id)
    	with open(f"{post.id}.{post.file.ext}", "wb") as f:
        	f.write(requests.get(post.file.url).content)
except Exception as e:
    print(f"❌ API Error: {e}")

