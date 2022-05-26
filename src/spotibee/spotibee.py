# SpotiBee: A simple program for Spotify hotkeys
# Copyright (C) 2022  BeeLover66
#
# See __init__.py for more information

import argparse
import spotify
import hotkey_manager as hotkeys
from sound import play
import keyboard


WELCOME = """         ____        ____        ____        ____        ____        ____        ____   
        /    \\      /    \\      /    \\      /    \\      /    \\      /    \\      /    \\  
   ____/      \\____/      \\____/      \\____/      \\____/      \\____/      \\____/      \\ 
  /    \\      /    \\      /    \\      /    \\      /    \\      /    \\      /    \\      / 
 /      \\____/      \\____/      \\____/      \\____/      \\____/      \\____/      \\____/  
 \\      /    \\      /    \\      /    \\      /    \\      /    \\      /    \\      /    \\  
  \\____/      \\____/      \\____/      \\____/      \\____/      \\____/      \\____/      \\ 
  /    \\      /    \\    ╔═══╗╔═══╗╔═══╗╔════╗╔══╗╔══╗ ╔═══╗╔═══╗   \\      /    \\      / 
 /      \\____/      \\___║╔═╗║║╔═╗║║╔═╗║║╔╗╔╗║╚╣╠╝║╔╗║ ║╔══╝║╔══╝    \\____/      \\____/  
 \\      /    \\      /   ║╚══╗║╚═╝║║║ ║║╚╝║║╚╝ ║║ ║╚╝╚╗║╚══╗║╚══╗    /    \\      /    \\  
  \\____/      \\____/    ╚══╗║║╔══╝║║ ║║  ║║   ║║ ║╔═╗║║╔══╝║╔══╝___/      \\____/      \\ 
  /    \\      /    \\    ║╚═╝║║║   ║╚═╝║ ╔╝╚╗ ╔╣╠╗║╚═╝║║╚══╗║╚══╗   \\      /    \\      / 
 /      \\____/      \\___╚═══╝╚╝   ╚═══╝ ╚══╝ ╚══╝╚═══╝╚═══╝╚═══╝    \\____/      \\____/  
 \\      /    \\      /    \\      / A simple program for  /    \\      /    \\      /    \\  
  \\____/      \\____/      \\____/ global Spotify hotkeys/      \\____/      \\____/      \\ 
  /    \\      /    \\      /    \\      /    \\      /    \\      /    \\      /    \\      / 
 /      \\____/      \\____/      \\____/      \\____/      \\____/      \\____/      \\____/  
 \\      /    \\      /    \\      /    \\      /    \\      /    \\      /    \\      /       
  \\____/      \\____/      \\____/      \\____/      \\____/      \\____/      \\____/        
                                                                                        """

exit_state = False


def main():
    auth_file, hotkeys_file = parse_args()

    sp = spotify.init(auth_file)
    
    exit_hk = hotkeys.HotkeyManager(sp, hotkeys_file).exit_hk

    print(WELCOME)
    play("startup")

    keyboard.wait(exit_hk)

    play("shutdown", True)


def parse_args():
    parser = argparse.ArgumentParser(description="SpotiBee: A simple program for global Spotify hotkeys")
    parser.add_argument("-a", "--auth_file",
                        help="Path to JSON file containing the values of client_id and redirect_uri. Default is "
                             "assets/json/authorization.json",
                        required=False, default="assets/json/authorization.json")
    parser.add_argument("-k", "--hotkeys_file",
                        help="Path to JSON file containing the hotkeys of play_pause, save_unsave, skip, exit, "
                             "mute and info. Default is assets/json/hotkeys.json",
                        required=False, default="assets/json/hotkeys.json")

    argument = parser.parse_args()

    return argument.auth_file, argument.hotkeys_file


if __name__ == "__main__":
    main()
