#!/usr/bin/python
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from e621 import E621  # New library import
from dotenv import load_dotenv
load_dotenv()
import requests
import json
import os
from firebase import firebase

app = Flask(
    __name__,
    template_folder='../templates',
    static_folder='../static',
    static_url_path='/static'
)

emulatorjs_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'EmulatorJS'))

@app.route("/")
def home():
    return render_template("frontpage.html")

# Read them securely
USER_AGENT = os.getenv("E621_USER_AGENT")
USERNAME = os.getenv("E621_USERNAME")
API_KEY = os.getenv("E621_API_KEY")

auth = (USERNAME, API_KEY)

# Ensure E621 client receives exactly 2 items to unpack
client = E621(auth)

# Firebase setup (uncomment and provide your URL)
# firebase_app = firebase.FirebaseApplication('your_firebase_url', None)

SEARCH_LIMIT = 20
BLACKLIST_TAGS = "-underage -cub -vore -fart -macro -diaper -feral -human -dbz -mpreg -sega"
dir_path = os.path.dirname(os.path.realpath(__file__))
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
image_dir = os.path.join(project_root, 'static', 'images')
JSON_FILE = os.path.join(image_dir, 'search.json')

if not os.path.exists(image_dir):
    os.makedirs(image_dir)

def default_json_serializer(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

@app.route('/search', methods=['GET'])

def search():
    search_tags = request.args.get('tags', '').strip()
    rating = request.args.get('rating', '').strip()

    # Only fetch if tags are provided
    if search_tags:
        query = f"{search_tags} {rating} order:random status:active {BLACKLIST_TAGS}"
        try:
            results = client.posts.search(tags=query, limit=SEARCH_LIMIT)
        except Exception as e:
            return f"<h1>API Error: {e}</h1>"

        # 🧹 Clean up previous images
        delete_images()
        
        # Save JSON data
        with open(JSON_FILE, 'w') as f:
            posts_data = []
            for post in results:
                try:
                    posts_data.append(post.dict(exclude={"e621api"}))
                    #print(posts_data)
                except Exception as e:
                    print(f"Serialization error for post {getattr(post, 'id', 'unknown')}: {e}")
            json.dump(posts_data, f, indent=4, default=default_json_serializer)

        # Download images
        downloaded_images = fetch_images(results)

        return render_template('answer.html', tags=search_tags, rating=rating, images=downloaded_images)

    # No search performed yet — show page with form only
    return render_template('answer.html', tags=None, rating=None, images=None)

def fetch_images(data):
    downloaded = []
    for post in data:
        try:
            url = post.file.url
            post_id = post.id

            if not url:
                continue

            ext = url.split('.')[-1].lower()
            if ext not in ['jpg', 'png']:
                continue

            filename = f"{post_id}.{ext}"
            filepath = os.path.join(image_dir, filename)

            if os.path.exists(filepath):
                downloaded.append(f"images/{filename}")
                continue

            response = requests.get(url)
            if response.status_code == 200:
                with open(filepath, 'wb') as f:
                    f.write(response.content)
                downloaded.append(f"images/{filename}")
                print(f"Saved: {filepath}")
            else:
                print(f"Failed to fetch: {url} [{response.status_code}]")
        except Exception as e:
            print(f"Error downloading post {getattr(post, 'id', 'unknown')}: {e}")

    return downloaded

def delete_images():
    for file in os.listdir(image_dir):
        if file.endswith(('.jpg', '.jpeg', '.png')):
            try:
                os.remove(os.path.join(image_dir, file))
            except Exception as e:
                print(f"Could not delete {file}: {e}")

@app.route('/submit_message', methods=['POST'])
def submit_message():
    message = {
        'body': request.form.get('message', ''),
        'who': request.form.get('who', '')
    }
    # firebase_app.post('/messages', message)  # Uncomment when Firebase is set up
    return redirect(url_for('index'))


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name').strip()
        email = request.form.get('email').strip()
        message = request.form.get('message').strip()

        # Simple validation
        if not name or not email or not message:
            return render_template('contact.html', error="All fields are required.")

        # Here you would process the message: send email, save to DB, etc.
        # For now, just print to console as an example:
        print(f"New message from {name} ({email}):\n{message}")

        return render_template('contact.html', success=True)

    return render_template('contact.html')

# Serve EmulatorJS index.html
@app.route('/emulator')
def emulator_index():  
    print("Serving EmulatorJS from:", emulatorjs_path)
    return send_from_directory(emulatorjs_path, 'index.html')

# Serve EmulatorJS static files under /emulatorjs/*
@app.route('/emulatorjs/<path:filename>')
def serve_emulatorjs_file(filename):
    return send_from_directory(emulatorjs_path, filename)

@app.route('/emulatorjs/data/<path:filename>')
def serve_emulatorjs_data(filename):
    return send_from_directory(os.path.join(emulatorjs_path, 'data'), filename)

@app.route('/emulatorjs/docs/<path:filename>')
def serve_emulatorjs_docs(filename):
    return send_from_directory(os.path.join(emulatorjs_path, 'docs'), filename)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
