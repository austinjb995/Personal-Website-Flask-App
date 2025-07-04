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


