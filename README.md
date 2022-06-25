# SpotiBee: A simple program for global Spotify hotkeys

![Contributors](https://img.shields.io/github/contributors/BeeLover66/SpotiBee)
![Forks](https://img.shields.io/github/forks/BeeLover66/SpotiBee)
![Stars](https://img.shields.io/github/stars/BeeLover66/SpotiBee)
![Licence](https://img.shields.io/github/license/BeeLover66/SpotiBee)
![Issues](https://img.shields.io/github/issues/BeeLover66/SpotiBee)

## Description

This application was made with the purpose of interacting with Spotify 
without needing to alt-tab out of your favorite application or game. It 
implements custom hotkeys to automate simple tasks, such as pausing the 
currently playing song or saving it to the user's "My Library" playlist. 
Sound effects are also played to confirm the execution of the action.

### Currently supported actions

- Pause or resume the user's playback (Spotify Premium only)
- Save to or remove from the user's Your Library playlist.
- Skip the user's playback to the next track. (Spotify Premium only)
- Use text to speech to give the song and artist names of the user's 
currently playing track.
- Mute or unmute the program's sound effects

## Installing and using

If you only want to use the program without modifying the source code, 
download the latest release [here](https://github.com/BeeLover66/SpotiBee/releases). 
You can then extract the archive wherever you prefer. To launch the 
program, simply execute the spotibee.exe file present in the spotibee 
directory. You may need to tell any antivirus program that the program is 
safe in order to execute it.

For now, the Spotify App used to make API calls is in development mode, 
therefore only 25 accounts can use the program simultaneously. If you do 
not know me personally, you should consider creating your own Spotify App 
[here](https://developer.spotify.com/dashboard/) and change the client ID 
in the authorization.json file.

You can edit the hotkeys via the assets/json/hotkeys.json file. The hotkey
must be in the format `"ctrl+shift+a, s"`. This would trigger when the 
user holds ctrl, shift and "a" at once, releases, and then presses "s". To
represent literal commas, pluses, and spaces, use their names 
('comma', 'plus','space').

You can also replace the sound effect files in the assets/sound/ 
directory, as long as they have the same name and file extension (mp3) as 
the original ones.

The executable was created with pyinstaller using the spotibee.spec file.

## Contributing

Contibutions, issues and feature requests are welcome. <br>
You can check out the issues page [here](https://github.com/BeeLover66/SpotiBee/issues).

## License

Copyright (C) 2022  [BeeLover66](https://github.com/BeeLover66)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

SpotiBee uses the following libraries, which are all licensed under the 
[MIT license](https://choosealicense.com/licenses/mit/):
- [gTTS](https://github.com/pndurette/gTTS)
- [keyboard](https://github.com/boppreh/keyboard)
- [playsound](https://github.com/TaylorSMarks/playsound)
- [spotipy](https://github.com/plamere/spotipy)