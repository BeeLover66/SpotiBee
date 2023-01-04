# SpotiBee: A simple program for Spotify hotkeys
# Copyright (C) 2022-2023  BeeLover66
#
# See __init__.py for more information

import spotify

import hotkey_manager as hotkeys
from sound import play
import keyboard


AUTH_PATH = "assets/json/authorization.json"
HOTKEYS_PATH = "assets/json/hotkeys.json"

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
    auth_file, hotkeys_file = AUTH_PATH, HOTKEYS_PATH

    sp = spotify.init(auth_file)
    
    exit_hk = hotkeys.HotkeyManager(sp, hotkeys_file).exit_hk

    print(WELCOME)
    play("startup")

    keyboard.wait(exit_hk)

    play("shutdown", True)


if __name__ == "__main__":
    main()
