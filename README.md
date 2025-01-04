Discord Music Bot with Spotify and YouTube Integration
Opis
Ten bot Discord pozwala na odtwarzanie muzyki z YouTube i Spotify, zarządzanie kolejką utworów oraz obsługę komend umożliwiających kontrolowanie odtwarzania muzyki na serwerze Discord. Bot obsługuje wszystkie podstawowe operacje związane z odtwarzaniem muzyki, a także oferuje bardziej zaawansowane funkcje, takie jak logowanie zdarzeń i błędów, czy zarządzanie kanałami głosowymi.

Projekt został stworzony w Pythonie i jest zoptymalizowany do uruchomienia w kontenerze Docker, co umożliwia łatwą instalację i uruchomienie na serwerze.

Funkcje
🎵 Odtwarzanie muzyki z YouTube i Spotify
Bot pozwala na dodawanie utworów z YouTube oraz Spotify do kolejki i ich odtwarzanie. Obsługuje pełne integracje API tych platform, umożliwiając płynne streamowanie muzyki. Możesz po prostu wkleić link do utworu lub playlisty, a bot automatycznie go pobierze i zacznie odtwarzać.

📜 Zarządzanie kolejką
Użytkownicy mogą dodawać, pomijać oraz wyświetlać aktualną kolejkę utworów. Kolejka jest dynamicznie zarządzana, a bot zawsze odtwarza następny utwór po zakończeniu obecnego. Można także usunąć utwory z kolejki w trakcie odtwarzania.

⏹️ Zatrzymywanie muzyki i czyszczenie kolejki
Bot oferuje funkcję zatrzymywania muzyki oraz czyszczenia kolejki, co pozwala na pełną kontrolę nad sesją odtwarzania.

🔊 Obsługa kanałów głosowych
Bot dołącza do kanałów głosowych na serwerze Discord i obsługuje polecenia do opuszczania kanałów. Użytkownicy mogą również sterować odtwarzaniem w obrębie różnych kanałów.

📜 Logowanie
Bot zapisuje wszystkie zdarzenia oraz błędy do pliku bot.log, co pozwala na łatwiejszą diagnostykę w przypadku problemów. Logowanie obejmuje zarówno operacje na kolejce, jak i ewentualne błędy w trakcie próby połączenia z platformami zewnętrznymi.

Struktura projektu
1. Pliki źródłowe
bot.py: Główny plik uruchamiający bota, zawierający logikę interakcji z Discordem i integrację z API Spotify i YouTube.
queue.py: Plik zarządzający logiką kolejki utworów, zapewniający dodawanie, usuwanie i przeglądanie kolejki.
audio.py: Odpowiada za przetwarzanie audio i zarządzanie odtwarzaniem muzyki.
utils.py: Zawiera funkcje pomocnicze, takie jak logowanie, obsługa błędów i inne użyteczne metody.
config.json: Plik konfiguracyjny, który przechowuje dane uwierzytelniające API i ustawienia bota.
2. Integracja z YouTube i Spotify
YouTube: Używa yt-dlp do pobierania i dekodowania strumieni audio z YouTube.
Spotify: Wykorzystuje API Spotify do wyszukiwania utworów i playlist oraz odtwarzania ich za pomocą bota.
3. Docker
Projekt zawiera plik Dockerfile, który umożliwia łatwe stworzenie obrazu Dockera do uruchomienia bota w kontenerze. Docker pozwala na uproszczenie procesu instalacji oraz uruchomienia, minimalizując zależności środowiskowe.

Dockerfile
Skopiuj kod
# Plik Dockerfile
FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["python", "bot.py"]
4. Wymagania
Python 3.8+
Biblioteki:
discord.py (do obsługi API Discord)
yt-dlp (do ściągania audio z YouTube)
spotipy (do obsługi Spotify)
asyncio (do obsługi asynchronicznych operacji)
Instrukcja uruchomienia
Skonfiguruj środowisko

Skopiuj plik config.json do folderu z projektem i wprowadź swoje dane API dla Spotify oraz inne niezbędne ustawienia.
Zainstaluj wymagane biblioteki W terminalu uruchom:

bash
Skopiuj kod
pip install -r requirements.txt
Uruchom bota W terminalu uruchom:

bash
Skopiuj kod
python bot.py
Docker Jeśli chcesz uruchomić bota w Dockerze, wykonaj:

bash
Skopiuj kod
docker build -t discord-music-bot .
docker run -d discord-music-bot

############################################################################################################################

Discord Music Bot with Spotify and YouTube Integration
Description
This Discord bot allows you to play music from YouTube and Spotify, manage the queue, and use commands to control playback on your Discord server. The bot supports all basic music operations and offers advanced features like event and error logging, and management of voice channels.

The project is created in Python and optimized to run in a Docker container, making it easy to install and launch on a server.

Features
🎵 Play Music from YouTube and Spotify
The bot allows you to add songs from YouTube and Spotify to the queue and play them. It fully integrates with the APIs of these platforms, enabling smooth music streaming. You can simply paste a link to a song or playlist, and the bot will automatically fetch and start playing it.

📜 Queue Management
Users can add, skip, and view the current music queue. The queue is dynamically managed, and the bot always plays the next song when the current one finishes. You can also remove songs from the queue during playback.

⏹️ Stop Music and Clear Queue
The bot offers functionality for stopping music and clearing the queue, allowing full control over the playback session.

🔊 Voice Channel Support
The bot joins voice channels on the Discord server and supports commands to leave channels. Users can also control playback within different channels.

📜 Logging
The bot logs all events and errors into a bot.log file, which helps diagnose issues if they arise. Logging includes both queue operations and any errors when attempting to connect to external platforms.

Project Structure
1. Source Files
bot.py: The main file that runs the bot, containing logic for interacting with Discord and integrating with the YouTube and Spotify APIs.
queue.py: A file that manages the logic for the music queue, allowing adding, removing, and viewing the queue.
audio.py: Responsible for audio processing and managing music playback.
utils.py: Contains helper functions like logging, error handling, and other useful methods.
config.json: The configuration file storing API credentials and bot settings.
2. YouTube and Spotify Integration
YouTube: Uses yt-dlp to download and decode audio streams from YouTube.
Spotify: Uses the Spotify API to search for songs and playlists and play them through the bot.
3. Docker
The project includes a Dockerfile that allows for easy creation of a Docker image to run the bot inside a container. Docker simplifies the installation and running process, minimizing environmental dependencies.

Dockerfile
Skopiuj kod
# Dockerfile
FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["python", "bot.py"]
4. Requirements
Python 3.8+
Libraries:
discord.py (for Discord API handling)
yt-dlp (for downloading audio from YouTube)
spotipy (for Spotify API integration)
asyncio (for handling asynchronous operations)
How to Run
Set Up the Environment

Copy the config.json file to your project folder and enter your API credentials for Spotify and other necessary settings.
Install Required Libraries In the terminal, run:

bash
Skopiuj kod
pip install -r requirements.txt
Run the Bot In the terminal, run:

bash
Skopiuj kod
python bot.py
Docker If you want to run the bot in Docker, use:

bash
Skopiuj kod
docker build -t discord-music-bot .
docker run -d discord-music-bot
