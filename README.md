# Personal Website Flask App

> ⚠️ **WARNING**  
> This application integrates with the [e621.net](https://e621.net) API, a community-driven image board that may serve **NSFW or adult content**. Viewer discretion is advised.  
> By using this app, you acknowledge and accept the responsibility for any content retrieved via search queries.

---

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

---

## Requirements

- Python 3.11+
- Git
- pip / virtualenv

## Python Dependencies

Make sure you are using a virtual environment:

```bash
python3 -m venv webdev
source webdev/bin/activate
pip install -r requirements.txt


