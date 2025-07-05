# Personal Website Flask App

> ⚠️ **WARNING**  
> This application integrates with the [e621.net](https://e621.net) API, a community-driven image board that may serve **NSFW or adult content**. Viewer discretion is advised.
>   
> By using this app, you acknowledge and accept the responsibility for any content retrieved via search queries or of your own curiosity.
> If you want to see a similar Flask App that is more "Professional" please see this repo that uses Unsplash instead of e621.net API. [`Unsplash Flask App`](https://github.com/austinjb995/Unsplash-Project).
> If you accidentally see something you do not like have some [`eye-bleach`](https://eyebleach.me/).
> 
> If you would like to view the API in action, I would stick with the safe rating. I did my best to filter out the worse the site has to offer, but I can not guarantee something wont slip through the cracks. I apologize in advance.
> The purpose of this project was to have an enjoyable and fun project that I can continously want to work on and improve as I am more personally connected to it.

---

This Project is still a WIP and may not work fully. Some features like the About This Site, message board, and Contact Me do not work/have not been fully implemented. I have gotten this site working fully on the e621 API and EmulatorJS up and running.
I will update this ReadMe as I go along with this project.

## Overview

This is a Flask-based personal website and web application with the following features:

- Image search with rating/tag filters using the e621 API.
- Retro game emulation using [EmulatorJS](https://github.com/EmulatorJS/EmulatorJS).
- Optional message handling through Firebase.
- Simple contact form.
- Static asset delivery (CSS, images).
- Server-side image caching and cleanup.
- Supports environment variables via `.env`.

---

## e621-py Wrapper & Fork Justification

This project uses [`e621-py`](https://github.com/eoan-ermine/e621-py), a Python wrapper for the [e621 API](https://e621.net/help/api).  
However, the original package does not fully serialize `Post` models due to recent changes in the API schema and missing fields, causing runtime errors and broken JSON conversion.

To resolve this, the following improvements were made and are included in a fork:

📌 **Forked Repository:**  
**https://github.com/austinjb995/e621-py**

🔧 **Modifications Include:**
- Added fallback handling for missing `alternates` and `sample` fields in `Post` models.
- Custom serialization support for `set` objects to enable proper `json.dump()`.
- Updated client instantiation to accept `(username, api_key)` auth tuple securely.
- Tested compatibility with Pydantic v1.10.

This fork is referenced in the `requirements.txt` as:

```text
e621 @ git+https://github.com/austinjb995/e621-py.git@main
```
---

## Features

- 🔍 Search e621 content with filters and safety ratings.
- 🕹️ Play games through integrated EmulatorJS.
- 📬 Contact form for feedback.
- 🧼 Automatically cleans old image assets on new searches.

---

## 🧱 Requirements

This app requires Python 3.11+ and a virtual environment. Install dependencies from `requirements.txt`.

## Python Dependencies

Make sure you are using a virtual environment:

```bash
python3 -m venv webdev
source webdev/bin/activate
pip install -r requirements.txt
```
## EmulatorJS Set Up

Simply clone the EmulatorJS repo in the root directory of your project. I did this for simplicity and ease of use.

```bash
git clone https://github.com/EmulatorJS/EmulatorJS.git
```

## .env Configuration

Create a .env file with your e621.net API key and your username

```.env file contents
E621_USER_AGENT="MyApp/1.0 (by username on e621)"
E621_USERNAME="your_username"
E621_API_KEY="your_api_key"
```

## Project Structure

From your project root directory this is the general layout. 

```text
.
├── app/
│   ├── app.py
│   ├── ...
├── static/
│   └── images/
├── templates/
│   └── ...
├── EmulatorJS/
│   └── ...
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```
___

## Disclaimer

This is an unofficial project. Neither this app nor its author is affiliated with e621.net or EmulatorJS. All content fetched or rendered is subject to their respective licenses and terms of use.
