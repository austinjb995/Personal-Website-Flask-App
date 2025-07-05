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
- 📬 Contact form for feedback.
- 🧼 Automatically cleans old image assets on new searches.

## Possible Planned Features/Things I would like to add
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
