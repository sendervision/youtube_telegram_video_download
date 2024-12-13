# Telegram YouTube Downloader Bot

A Telegram bot that allows users to download videos or audio from YouTube in different formats (MP3, 720p, 360p, etc.). The bot uses the Telegram API and the `yt-dlp` library to extract videos and manage downloads.

---

## Features
- Download YouTube videos in various formats (MP3, 720p, 360p, etc.).
- Automatic MP3 conversion using FFmpeg.
- Deletes temporary files after sending them to the user.
- Interactive Telegram buttons for an intuitive user experience.

---

## Prerequisites
Before running the project, make sure you have:
1. **Python 3.8+** installed.
2. The following dependencies:
   - [`python-telegram-bot`](https://python-telegram-bot.readthedocs.io/)
   - [`yt-dlp`](https://github.com/yt-dlp/yt-dlp)
3. **FFmpeg** installed to convert audio files to MP3:
   - **Linux**: `sudo apt install ffmpeg`
   - **Mac**: `brew install ffmpeg`
   - **Windows**: Download it from [ffmpeg.org](https://ffmpeg.org).

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sendervision/youtube_telegram_video_download.git
   cd youtube_telegram_video_download
   ```

   
2. Install dependencies:

   ```bash
   pip install python-telegram-bot yt-dlp
   ```


3. Configure your Telegram bot:

Obtain a Telegram Bot Token from BotFather.

Replace "YOUR_TELEGRAM_TOKEN" in the main script with your bot token.


4. Run the bot:

   ```bash
   python main.py
   ```
---

Usage

1. Send a valid YouTube link to the bot.


2. The bot will reply with:

The video title.

The number of views.

The channel name.

Buttons to choose the download format.

3. Select the desired format. The bot will download the video or audio and send it to you.

---

Architecture

Key Libraries

python-telegram-bot: To handle Telegram interactions.

yt-dlp: To extract and download YouTube videos/audio.

FFmpeg: To convert audio files to MP3.


File Management

Downloaded files are deleted immediately after being sent to the user to avoid disk clutter.



---

Possible Improvements

Add handling for long videos by limiting file size or duration.

Integrate a caching system to avoid redownloading previously requested videos.

Deploy the bot to a server (VPS, Docker, etc.) for continuous availability.



---

License

This project is licensed under the MIT License. See the LICENSE file for details.
