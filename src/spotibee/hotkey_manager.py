# SpotiBee: A simple program for Spotify hotkeys
# Copyright (C) 2022  BeeLover66
#
# See __init__.py for more information

import keyboard
import json
import spotify
from sound import mute


class HotkeyManager:

    def __init__(self, sp, hotkeys_file):
        """
        Creates a group of global hotkeys that can send requests using a given Spotify API client.

        :param sp: The Spotify API client making the requests when a hotkey is pressed :param hotkeys_file: local
        path to the file containing the hotkeys for play_pause, save_unsave, skip, mute, info and exit
        """
        self.sp = sp

        with open(hotkeys_file) as f:
            hotkey_config = json.load(f)

        name_to_func = {
            "play_pause": self.play_pause,
            "save_unsave": self.save_unsave,
            "skip": self.skip,
            "info": self.info,
            "mute": mute
        }

        hotkeys = {}
        for name, func in name_to_func.items():
            if name in hotkey_config:
                hotkeys[hotkey_config[name]] = func

        self.exit_hk = hotkey_config["exit"]

        if None in hotkeys:
            hotkeys.pop(None)

        for hotkey, func in hotkeys.items():
            try:
                keyboard.add_hotkey(hotkey=hotkey, callback=func)
            except ValueError:
                print(f"WARNING: hotkey '{hotkey}' could not be parsed.")

    def play_pause(self):
        spotify.play_pause(self.sp)

    def save_unsave(self):
        spotify.save_unsave(self.sp)

    def skip(self):
        spotify.skip(self.sp)

    def info(self):
        spotify.info(self.sp)
