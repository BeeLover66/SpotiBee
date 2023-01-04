# SpotiBee: A simple program for Spotify hotkeys
# Copyright (C) 2022-2023  BeeLover66
#
# See __init__.py for more information

import keyboard
import json
import spotify
from sound import mute_effects


class HotkeyManager:
    """
    Manages a group of global hotkeys that can send requests using a given Spotify API client.
    """

    def __init__(self, sp, hotkeys_file):
        """
        Creates the hotkeys by parsing the JSON file and initializes them all.

        :param sp: The Spotify API client making the requests when a hotkey is pressed
        :param hotkeys_file: local path to the file containing the hotkeys for play_pause, save_unsave, skip, mute,
        info and exit
        """
        self.sp = sp

        with open(hotkeys_file) as f:
            hotkey_config = json.load(f)

        name_to_func = {
            "play_pause": (spotify.play_pause, [self.sp]),
            "save_unsave": (spotify.save_unsave, [self.sp]),
            "skip": (spotify.skip, [self.sp]),
            "info": (spotify.info, [self.sp]),
            "mute_effects": (mute_effects, [])
        }

        hotkeys = {}
        for name, func in name_to_func.items():
            if name in hotkey_config:
                hotkeys[hotkey_config[name]] = func

        if None in hotkeys:
            hotkeys.pop(None)

        # Exit hotkey, required to be in the JSON file
        if "exit" not in hotkey_config:
            print("ERROR: hotkeys.json does not contain a hotkey for 'exit'.")
            exit()
        self.exit_hk = hotkey_config["exit"]

        # Volume hotkeys, appear as a list in the JSON file
        if "volume" in hotkey_config:
            for volume_hk in hotkey_config["volume"]:
                try:
                    keyboard.add_hotkey(hotkey=volume_hk["hk"], callback=spotify.shift_volume,
                                        args=[self.sp, volume_hk["qty"]])
                except ValueError:
                    print("WARNING: one of the 'volume' hotkeys could not be parsed.")

        # Other hotkeys
        for hotkey, func in hotkeys.items():
            try:
                keyboard.add_hotkey(hotkey=hotkey, callback=func[0], args=func[1])
            except ValueError:
                print(f"WARNING: hotkey '{hotkey}' could not be parsed.")
