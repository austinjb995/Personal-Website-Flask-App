# Personal Website Flask App

> ⚠️ **WARNING**  
> This application integrates with the [e621.net](https://e621.net) API, a community-driven image board that may serve **NSFW or adult content**. Viewer discretion is advised.
>
> This is a personal full-stack project that interacts with a public API for an adult content platform. The intent was to challenge myself on API integration,and production-ready Flask deployment. While
> the content source is niche, the technical stack is fully transferable to mainstream use cases.
>
> That beind said, the website v0.9.0-beta pre-release is live at https://www.austinbell.xyz.

---

This Project is in its infancy stage and may not work fully. Some features like the About This Site, message board, and Contact Me do not work/have not been fully implemented. I have gotten this site working fully on the e621 API and EmulatorJS up and running. I will update this ReadMe as I go along with this project and refine it.

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

## Features

- 🔍 Search e621 content with filters and safety ratings.
- 🕹️ Play games through integrated EmulatorJS.
- 🧼 Automatically cleans old image assets on new searches.

## Upcoming Milestones
v0.9.1-beta
**Anonymous Comment System**
    - Add SQLite or PostgreSQL backend (configurable)
    - Comment schema: post_id, comment, timestamp, ip_hash
    - Front-end form with client-side JS validation
    - Admin-only endpoint to view/delete comments

**"Contact Me" Page**
    - HTML form to send messages (via SMTP or Mailgun API)
    - Backend validation and spam filtering
    - Flash message or modal confirmation

**About This Site Page**
    - Static HTML page in templates/about.html
    - Brief description of tech stack and privacy policies
    - Navigation link added to main layout

## Milestones I Would Add In the Future
- Something more immediate would be an 18+ Age verification prompt
- Support for other image boards
- Making everything more "pretty" i.e more front end work with CSS and JS
- Add the most used tags for reference in answer.html
- Implement a popular button to cache and display popular images on e621

---
# Automated Install Script

Go to the releases page and download the install.sh script for an automated install (POSIX Compliant). Simply make it executable and running the script in your desired location.

```shell
chmod +x ./install.sh
./install.sh
```
This is the simplest way to make it as it runs all the commands neccessary for setup. Manual installation is below if you want to do it the manual way.


# Manual Installation Below 

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
git clone https://www.github.com/EmulatorJS/EmulatorJS.git
```

## .env Configuration

Create a .env file with your e621.net API key and your username

```.env file contents
E621_USER_AGENT="MyApp/1.0 (by username on e621)"
E621_USERNAME="your_username"
E621_API_KEY="your_api_key"
```

## 401 Error

If you get this error, that means you need to setup your API key (you need to make an e621 account to get an API key).

```error
API Error: 401 Client Error: Unauthorized for url: 
```
___

## Disclaimer

This is an unofficial project. Neither this app nor its author is affiliated with e621.net or EmulatorJS. All content fetched or rendered is subject to their respective licenses and terms of use.
