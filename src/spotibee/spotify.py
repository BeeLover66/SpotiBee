# SpotiBee: A simple program for Spotify hotkeys
# Copyright (C) 2022  BeeLover66
#
# See __init__.py for more information

import spotipy  # https://spotipy.readthedocs.io/en/2.19.0/
from spotipy.oauth2 import SpotifyPKCE
import json
from sound import play, tts


def init(auth_json):
    """
    Creates a Spotify API client using the PKCE Auth flow

    The client_id and redirect_uri are read from the authorization.json file

    :type auth_json: str
    :param auth_json: local path to the file containing the client_id and redirect_uri
    :return: The created Spotify API client
    """
    with open(auth_json) as f:
        credentials = json.load(f)
    client_id = credentials["client_id"]
    redirect_uri = credentials["redirect_uri"]

    # https://developer.spotify.com/documentation/general/guides/authorization/scopes/#user-library-modify
    scope = ["user-library-modify",
             "user-library-read",
             "user-modify-playback-state",
             "user-read-currently-playing",
             "user-read-playback-state",
             "user-read-private"]

    auth_manager = SpotifyPKCE(client_id=client_id,
                               redirect_uri=redirect_uri,
                               scope=scope,
                               cache_handler=spotipy.CacheFileHandler())

    sp = spotipy.Spotify(auth_manager=auth_manager)

    return sp


def play_pause(sp):
    """
    Pauses / resumes user's playback.

    If user does not have Spotify Premium or there is no current playback, play error sound and send message explaining
    why the request could not be processed.

    :type sp: spotipy.Spotify
    :param sp: The Spotify API client to which to send the request
    """
    if sp.current_user()["product"] != "premium":
        print("I can't do that because your account doesn't have Spotify Premium...")
        play("error")
        return
    current_playback = sp.current_playback()
    if current_playback is None:
        print("I can't do that, nothing is playing!")
        play("error")
        return
    is_playing = current_playback["is_playing"]
    if is_playing:
        sp.pause_playback()
        print("playback paused")
    else:
        sp.start_playback()
        print("playback started")


def save_unsave(sp):
    """
    Saves to / removes from user's Your Library playlist.

    If there is no current playback, play error sound and send message explaining why the request could not be
    processed.

    :type sp: spotipy.Spotify
    :param sp: The Spotify API client to which to send the request
    """
    currently_playing = sp.currently_playing()
    if currently_playing is None:
        print("I can't do that, nothing is playing!")
        play("error")
        return
    current_uri = [currently_playing["item"]["uri"]]
    current_name = currently_playing["item"]["name"]
    if sp.current_user_saved_tracks_contains(tracks=current_uri)[0]:
        sp.current_user_saved_tracks_delete(tracks=current_uri)
        print("current track '{name}' removed from your library".format(name=current_name))
        play("unsave")
    else:
        sp.current_user_saved_tracks_add(tracks=current_uri)
        print("current track '{name}' saved to your library".format(name=current_name))
        play("save")


def skip(sp):
    """
    Skips user's playback to next track.

    If user does not have Spotify Premium or there is no current playback, play error sound and send message explaining
    why the request could not be processed.

    :type sp: spotipy.Spotify
    :param sp: The Spotify API client to which to send the request
    """
    if sp.current_user()["product"] != "premium":
        print("I can't do that because your account doesn't have Spotify Premium...")
        play("error")
        return
    if sp.current_playback() is None:
        print("I can't do that, nothing is playing!")
        play("error")
        return
    sp.next_track()


def info(sp):
    """
    Uses text to speech to give song and artist names of user's currently playing track.

    If there is no current playback, play error sound and send message explaining why the request could not be
    processed.

    :type sp: spotipy.Spotify

    :param sp: The Spotify API client to which to send the request
    """
    currently_playing = sp.currently_playing()

    if sp.current_playback() is None:
        print("I can't do that, nothing is playing!")
        play("error")
        return

    track_name = currently_playing["item"]["name"]
    artist_name = currently_playing["item"]["artists"][0]["name"]

    to_say = f"Currently playing: {track_name}, by {artist_name}."

    print(to_say)
    tts(to_say)
