# SpotiBee: A simple program for Spotify hotkeys
# Copyright (C) 2022-2023  BeeLover66
#
# See __init__.py for more information

from playsound import playsound
from gtts import gTTS
from os import remove as rm

SOUND_DIR = "assets/sound/"
SOUND_EXT = ".mp3"
TTS_FILE = "tts"

muted = False


def play(sound, block=False):
    """
    Uses the playsound library to play the requested sound if the user has not muted the program.

    :type sound: str
    :type block: bool
    :param sound: Name of the sound file to play, without the directory or file extension.
    :param block: Setting block to True halts the program until the sound has finished playing.
    """
    if not muted:
        playsound(SOUND_DIR+sound+SOUND_EXT, block)


def mute_effects():
    """
    Toggles the sound effects.
    """
    global muted
    # If the user wants to mute, play mute sound before muting
    play("mute")
    muted = not muted
    # If the user wants to unmute, play unmute sound after unmuting
    play("unmute")
    if muted:
        print("Sound effects muted")
    else:
        print("Sound effects unmuted")


def tts(to_say, lang="en", block=False):
    """
    Uses the gTTS text-to-speech API to say a string.

    :type to_say: str
    :type lang: str
    :type block: bool

    :param to_say: The string to say
    :param lang: The language (IETF language tag) to read the text in. Default is "en".
    :param block: Setting block to True halts the program until the sound has finished playing.
    """
    tts_obj = gTTS(text=to_say, lang=lang)
    tts_obj.save(SOUND_DIR+TTS_FILE+SOUND_EXT)

    play(TTS_FILE, block)

    rm(SOUND_DIR+TTS_FILE+SOUND_EXT)  # Delete tts file after playing it
