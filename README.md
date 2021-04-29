# NabettoBot

A Twitch bot that bets for you. (Written in Python)

****

## Installation and Setup

<!--1. ~~Make sure to install tesseract-ocr from the official [website](https://github.com/tesseract-ocr/tesseract/wiki/Downloads).~~ Currently not in use.

2. Install chromedriver and copy down the directory for later installation [website](https://chromedriver.chromium.org/downloads).

3. Go to the project directory and install requirements.txt-->

1. Go to [twitchapps.com/tmi](https://twitchapps.com/tmi) and get your OAuth token (if you don't have a Twitch.tv account make one, it's free).
2. Copy your Twitch username
3. Open a command prompt and go to the parent folder of the project (NabettoBot)
4. Using pip type `pip install -e .` or using pipx do `pipx install -e .`
5. After the installation type `nabetto -u YOUR_USERNAME -p YOUR_OAUTH_TOKEN --save --show-chat`
6. Now your credentials are cached, next time you can just invoke nabetto in any directory without having to specify your username or OAuth token.

```cmd
cd NabettoBot
pip install -r requirements.txt
```

****

## Running The Bot

```cmd
python -m nabettobot
```
