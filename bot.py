import os
import logging
import discord
from discord.ext import commands
import youtube_dl
import requests
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy

# Konfiguracja logowania
logging.basicConfig(
    filename="bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Pobieranie zmiennych środowiskowych
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
spotify_client_id = os.getenv("SPOTIFY_CLIENT_ID")
spotify_client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

# Konfiguracja Spotify API
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=spotify_client_id,
    client_secret=spotify_client_secret
))

# Ustawienia bota Discord
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

# Kolejka odtwarzania
music_queue = []
current_song = None

# Funkcja wysyłania powiadomień webhookiem
def send_webhook_message(message):
    if DISCORD_WEBHOOK_URL:
        try:
            payload = {"content": message}
            headers = {"Content-Type": "application/json"}
            response = requests.post(DISCORD_WEBHOOK_URL, json=payload, headers=headers)
            if response.status_code == 204:
                logging.info("Webhook message sent successfully!")
        except Exception as e:
            logging.error(f"Failed to send webhook message: {e}")

# Funkcja odtwarzania kolejnego utworu
def play_next(ctx, voice_client):
    global current_song
    if len(music_queue) > 0:
        current_song = music_queue.pop(0)
        source = discord.FFmpegPCMAudio(current_song['source'])
        voice_client.play(source, after=lambda e: play_next(ctx, voice_client))
        logging.info(f"Now playing: {current_song['title']}")
        send_webhook_message(f"🎶 Rozpoczęto odtwarzanie: **{current_song['title']}**")
    else:
        current_song = None

@bot.event
async def on_ready():
    logging.info(f"Bot {bot.user.name} jest online!")
    print(f"Bot {bot.user.name} jest online!")

# Obsługa błędów
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("❌ Nie znaleziono komendy. Spróbuj ponownie.")
    else:
        logging.error(f"Błąd: {error}")
        send_webhook_message(f"❗ Wystąpił błąd: {error}")
        await ctx.send("Wystąpił nieoczekiwany błąd. Skontaktuj się z administratorem.")

# Komenda odtwarzania z YouTube
@bot.command(name="play")
async def play(ctx, *, query):
    voice_channel = ctx.author.voice.channel
    if not voice_channel:
        await ctx.send("Musisz być na kanale głosowym, aby odtworzyć muzykę!")
        return

    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if not voice_client:
        voice_client = await voice_channel.connect()

    # Pobieranie audio z YouTube
    with youtube_dl.YoutubeDL({'format': 'bestaudio', 'noplaylist': 'True'}) as ydl:
        info = ydl.extract_info(query, download=False)
        url = info['formats'][0]['url']
        title = info.get('title', 'Nieznany tytuł')
        music_queue.append({'source': url, 'title': title})
        logging.info(f"Added to queue: {title}")

    send_webhook_message(f"🎵 Dodano do kolejki: **{title}** (YouTube)")
    await ctx.send(f"🎵 Dodano do kolejki: **{title}**")

    if not voice_client.is_playing():
        play_next(ctx, voice_client)

# Komenda wyświetlenia kolejki
@bot.command(name="queue")
async def queue(ctx):
    if len(music_queue) == 0:
        await ctx.send("Kolejka jest pusta!")
    else:
        queue_list = "\n".join([f"{i + 1}. {song['title']}" for i, song in enumerate(music_queue)])
        await ctx.send(f"🎶 Kolejka:\n{queue_list}")

# Komenda pomijania
@bot.command(name="skip")
async def skip(ctx):
    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice_client and voice_client.is_playing():
        voice_client.stop()
        await ctx.send("⏭ Pominięto utwór.")
        logging.info("Skipped current song.")
    else:
        await ctx.send("Nie odtwarzany jest żaden utwór.")

# Komenda odtwarzania Spotify
@bot.command(name="spotify")
async def spotify_play(ctx, *, query):
    voice_channel = ctx.author.voice.channel
    if not voice_channel:
        await ctx.send("Musisz być na kanale głosowym, aby odtworzyć muzykę!")
        return

    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if not voice_client:
        voice_client = await voice_channel.connect()

    # Pobieranie ścieżek Spotify
    try:
        results = sp.search(q=query, limit=1)
        track = results['tracks']['items'][0]
        title = track['name']
        artist = track['artists'][0]['name']
        music_queue.append({'source': f"{title} {artist}", 'title': f"{title} - {artist}"})
        await ctx.send(f"🎵 Dodano do kolejki: **{title}** - {artist}")
        logging.info(f"Added Spotify track to queue: {title} - {artist}")
    except IndexError:
        await ctx.send("❌ Nie znaleziono wyników na Spotify.")
        logging.warning(f"Spotify search failed for query: {query}")
        return

    if not voice_client.is_playing():
        play_next(ctx, voice_client)

# Komenda zatrzymywania
@bot.command(name="stop")
async def stop(ctx):
    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice_client and voice_client.is_playing():
        voice_client.stop()
        music_queue.clear()
        await ctx.send("⏹️ Muzyka zatrzymana i kolejka wyczyszczona.")
        logging.info("Music stopped and queue cleared.")
    else:
        await ctx.send("Nie ma muzyki do zatrzymania.")

# Komenda opuszczania kanału
@bot.command(name="leave")
async def leave(ctx):
    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice_client:
        await voice_client.disconnect()
        await ctx.send("Bot opuścił kanał głosowy.")
        logging.info("Bot disconnected from voice channel.")

# Uruchomienie bota
bot.run(os.getenv('DISCORD_TOKEN'))