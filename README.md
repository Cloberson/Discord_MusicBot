# Discord Music Bot with Spotify and YouTube Integration

This Discord bot allows you to play music from YouTube and Spotify, manage the queue, and use commands to control playback on your Discord server. The bot supports all basic music operations and offers advanced features like event and error logging, and management of voice channels.

The project is created in Python and optimized to run in a Docker container, making it easy to install and launch on a server.

---

## Features

🎵 **Play Music from YouTube and Spotify**  
The bot allows you to add songs from YouTube and Spotify to the queue and play them. It fully integrates with the APIs of these platforms, enabling smooth music streaming. You can simply paste a link to a song or playlist, and the bot will automatically fetch and start playing it.

📜 **Queue Management**  
Users can add, skip, and view the current music queue. The queue is dynamically managed, and the bot always plays the next song when the current one finishes. You can also remove songs from the queue during playback.

⏹️ **Stop Music and Clear Queue**  
The bot offers functionality for stopping music and clearing the queue, allowing full control over the playback session.

🔊 **Voice Channel Support**  
The bot joins voice channels on the Discord server and supports commands to leave channels. Users can also control playback within different channels.

📜 **Logging**  
The bot logs all events and errors into a `bot.log` file, which helps diagnose issues if they arise. Logging includes both queue operations and any errors when attempting to connect to external platforms.

---

## Project Structure

1. **Source Files**
   - `bot.py`: The main file that runs the bot, containing logic for interacting with Discord and integrating with the YouTube and Spotify APIs.
   - `queue.py`: A file that manages the logic for the music queue, allowing adding, removing, and viewing the queue.
   - `audio.py`: Responsible for audio processing and managing music playback.
   - `utils.py`: Contains helper functions like logging, error handling, and other useful methods.
   - `config.json`: The configuration file storing API credentials and bot settings.

2. **YouTube and Spotify Integration**
   - **YouTube**: Uses `yt-dlp` to download and decode audio streams from YouTube.
   - **Spotify**: Uses the Spotify API to search for songs and playlists and play them through the bot.

3. **Docker**
   - The project includes a `Dockerfile` that allows for easy creation of a Docker image to run the bot inside a container. Docker simplifies the installation and running process, minimizing environmental dependencies.

---

## Dockerfile

```Dockerfile
# Dockerfile
FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["python", "bot.py"]

```
Requirements
Python 3.8+
Libraries:
discord.py (for Discord API handling)
yt-dlp (for downloading audio from YouTube)
spotipy (for Spotify API integration)
asyncio (for handling asynchronous operations)
How to Run
1. Set Up the Environment
Copy the config.json file to your project folder and enter your API credentials for Spotify and other necessary settings.
2. Install Required Libraries
In the terminal, run:
```bash
pip install -r requirements.txt
```
---
3. Run the Bot
In the terminal, run:
```bash
python bot.py
```
---
4. Docker (Optional)
If you want to run the bot in Docker, use:
```bash
docker build -t discord-music-bot .
docker run -d discord-music-bot
```
---
Logging
The bot logs all events and errors into the bot.log file, which helps in diagnosing issues if they arise. Ensure you check the log for troubleshooting.
Contributing
Feel free to fork this repository, open issues, or submit pull requests. Contributions are always welcome!


